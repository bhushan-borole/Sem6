import numpy as np


class KMeans:
	def __init__(self, k=2, tol=0.001, max_iter=300):
		self.k = k
		self.tol = tol
		self.max_iter = max_iter


	# fitting method
	def fit(self, data):
		self.centroids = {}

		# assigning first k points as centroids for k clusters
		for i in range(self.k):
			self.centroids[i] = data[i]

		for i in range(self.max_iter):
			self.classification = {}

			for j in range(self.k):
				self.classification[j] = []

			for feature in data:
				dist = [np.linalg.norm(feature-self.centroids[centroid]) for centroid in self.centroids]
				classification = dist.index(min(dist))
				self.classification[classification].append(feature)

			prev_centroids = dict(self.centroids)

			for classification in self.classification:
				self.centroids[classification] = np.average(self.classification[classification], axis=0)

			print('Iteration {}: '.format(i+1))
			print('Classification: ', self.classification)
			print('Centroids: ', self.centroids)
			print('#'*8)

			# stopping condition of KMeans clustering
			if prev_centroids == self.centroids:
				break


	def predict(self, data):
		distances = [np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroids]
		classification = distances.index(min(distances))
		print(classification)
		return classification


if __name__ == '__main__':
	kmeans = KMeans()
	X = np.array([2, 4, 10, 12, 3, 20, 30, 11, 25])
	kmeans.fit(X)