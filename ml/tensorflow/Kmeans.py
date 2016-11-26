import tensorflow as tf
from random import choice, shuffle
from numpy import array
def TKMeansCluster(vectors, noofclusters):
	"""
	K-Means is a n*k demicisions Numpy array,
	n is k-D's number
	noofclusters is cluster num(int)
	"""
	noofclusters = int(noofclusters)
	assert noofclusters < len(vectors)

	dim = len(vectors[0])
	vector_indices = list(range(len(vectors)))
	shuffle(vector_indices)

	graph = tf.Graph()
	with graph.as_default():
		sess = tf.Session()

		centroids = [tf.Variable((vectors[vector_indices[i]]))
		for i in range(noofclusters)]

		# in order to place the classfiers
		centroid_value = tf.placeholder("float64", [dim])
		cent_assigns = []
		for centroid in centroids:
			cent_assigns.append(tf.assign(centroid, centroid_value))

		assignments = [tf.Variable(0) for i in range(len(vectors))]
		assignment_value = tf.placeholder("int32")
		cluster_assigns = []
		for assignment in assignments:
			cluster_assigns.append(tf.assign(assignment, 
				assignment_value))

		# Placeholder for input
		mean_input = tf.placeholder("float", [None, dim])
		mean_op = tf.reduce_mean(mean_input, 0)

		# node in order to computer distance
		v1 = tf.placeholder("float", [dim])
		v2 = tf.placeholder("float", [dim])
		euclid_dist = tf.sqrt(tf.reduce_sum(tf.pow(tf.sub(
			v1, v2), 2)))

		# Place holder for imput 
		centroid_distances = tf.placeholder("float", [noofclusters])
		cluster_assignment = tf.argmin(centroid_distances, 0)

		# init all state value
		init_op = tf.initialize_all_variables()
		sess.run(init_op)

		noofiterations = 100
		for iteration_n in range(noofiterations):

			for vector_n in range(len(vectors)):
				vect =  vectors[vector_n]
				distances = [sess.run(euclid_dist, feed_dict = {
					v1;vect, v2: sess.run(centroid)
					})
				for centroid in centroids]

				assignment = sess.run(cluster_assignment, feed_dict = {
					centroid_distances: distances
					})
				sess.run(cluster_assigns[vector_n], feed_dict = {
					assignment_value:assignment
					})

			for cluster_n in range(noofclusters):

				assigned_vects = [vectors[i] for i in range(len(vectors))
				if sess.run(assignments[i]) == cluster_n]

				new_location = sess.run(mean_op, feed_dict = {
					mean_input: array(assigned_vects)
					})
				sess.run(cent_assigns[cluster_n], feed_dict = {
					centroid_value: new_location
					})
			centroids = sess.run(centroids)
			assignments = sess.run(assignments)
			return centroids, assignments


