import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

fishLength = [25.4, 26.3, 29.0, 9.8, 10.5, 11.0]
fishWeight = [242.0, 290.0, 363.0, 6.7, 7.5, 9.7]

fishTarget = [0, 0, 0, 1, 1, 1]

fishData = [[l, w] for l, w in zip(fishLength, fishWeight)]

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(fishData, fishTarget)

markers = ['o', 'x']
colors = ['red', 'blue']

plt.figure(figsize=(10, 6))

for i in range(2):
    targetIdx = [j for j in range(len(fishTarget)) if fishTarget[j] == i]
    
    plt.scatter(
        [fishLength[j] for j in targetIdx],
        [fishWeight[j] for j in targetIdx],
        marker=markers[i],
        color=colors[i],
        label=f'Type {i+1}'
    )

plt.xlabel('Length')
plt.ylabel('Weight')
plt.title('2 Fish Types Classification')
plt.legend()
plt.show()
