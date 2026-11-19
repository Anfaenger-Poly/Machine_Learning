import keras

model = keras.dmodels.load_model('best-cnn-model.keras')
print(model.layers)


