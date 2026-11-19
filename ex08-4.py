import os
import numpy as np
import keras
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.model_selection import train_test_split

# ---------------------------------------------------------------
# 1. 데이터 불러오기 (폴더 이름 = 클래스 이름)
# ---------------------------------------------------------------
DATA_DIR = '/mnt/c/Users/user/Desktop/28x28'
if not os.path.isdir(DATA_DIR):
    DATA_DIR = r'C:\Users\user\Desktop\28x28'

class_names = sorted(d for d in os.listdir(DATA_DIR)
                     if os.path.isdir(os.path.join(DATA_DIR, d)))
print('클래스:', class_names)

images, labels = [], []
for label, name in enumerate(class_names):
    folder = os.path.join(DATA_DIR, name)
    for fname in sorted(os.listdir(folder)):
        if not fname.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
        # 흑백 1채널로 통일
        img = Image.open(os.path.join(folder, fname)).convert('L').resize((28, 28))
        images.append(np.array(img))
        labels.append(label)

data = np.array(images).reshape(-1, 28, 28, 1) / 255.0
target = np.array(labels)
print('전체 데이터:', data.shape, target.shape, np.bincount(target))

# ---------------------------------------------------------------
# 2. 훈련 / 검증 / 테스트 분할 (클래스 비율 유지: stratify)
# ---------------------------------------------------------------
train_scaled, test_scaled, train_target, test_target = train_test_split(
        data, target, test_size=0.2, random_state=42, stratify=target)
train_scaled, val_scaled, train_target, val_target = train_test_split(
        train_scaled, train_target, test_size=0.2, random_state=42, stratify=train_target)
print('train:', train_scaled.shape, 'val:', val_scaled.shape, 'test:', test_scaled.shape)

# ---------------------------------------------------------------
# 3. 합성곱 신경망
# ---------------------------------------------------------------
model = keras.Sequential()
model.add(keras.layers.Input(shape=(28, 28, 1)))
# 데이터가 적어서(약 570장) 과대적합을 줄이기 위한 증강 (훈련 때만 동작)
model.add(keras.layers.RandomRotation(0.05))
model.add(keras.layers.RandomZoom(0.1))
model.add(keras.layers.RandomTranslation(0.1, 0.1))

model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu', padding='same'))
model.add(keras.layers.MaxPooling2D(2))

model.add(keras.layers.Conv2D(64, kernel_size=3, activation='relu', padding='same'))
model.add(keras.layers.MaxPooling2D(2))

model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dropout(0.4))
model.add(keras.layers.Dense(len(class_names), activation='softmax'))

model.summary()

# ---------------------------------------------------------------
# 4. 컴파일 및 훈련
# ---------------------------------------------------------------
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-photo-model.keras', save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)
history = model.fit(train_scaled, train_target, epochs=100, batch_size=32,
                    validation_data=(val_scaled, val_target),
                    callbacks=[checkpoint_cb, early_stopping_cb])

# 손실 / 정확도 그래프
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(history.history['loss'], label='train')
axs[0].plot(history.history['val_loss'], label='val')
axs[0].set_xlabel('epoch')
axs[0].set_ylabel('loss')
axs[0].legend()
axs[1].plot(history.history['accuracy'], label='train')
axs[1].plot(history.history['val_accuracy'], label='val')
axs[1].set_xlabel('epoch')
axs[1].set_ylabel('accuracy')
axs[1].legend()
plt.show()

# ---------------------------------------------------------------
# 5. 평가 (테스트 세트는 마지막에 한 번만)
# ---------------------------------------------------------------
test_loss, test_acc = model.evaluate(test_scaled, test_target)
print(f'테스트 정확도: {test_acc:.4f}')

# ---------------------------------------------------------------
# 6. 예측 확인: 종류별로 테스트 사진 1장씩
# ---------------------------------------------------------------
# 각 클래스에서 테스트 사진을 하나씩 고름
idx = [np.where(test_target == c)[0][0] for c in range(len(class_names))]
pred = model.predict(test_scaled[idx])
fig, axs = plt.subplots(1, len(class_names), figsize=(2.5 * len(class_names), 3))
for k, i in enumerate(idx):
    axs[k].imshow(test_scaled[i].reshape(28, 28), cmap='gray')
    p = np.argmax(pred[k])
    t = test_target[i]
    axs[k].set_title(f'pred: {class_names[p]}\ntrue: {class_names[t]}', fontsize=9,
                     color='black' if p == t else 'red')
    axs[k].axis('off')
plt.show()

model.save('best-photo-model-final.keras')
