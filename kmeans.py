# Make a 3D plot of k-means calculated clusters
# Guided by http://benalexkeen.com/k-means-clustering-in-python/  
# Get data ready
x = np.array(music['energy'])
y = np.array(music['valence'])
# Normalize tempo
z = np.array(music['tempo'])/211
df = pd.DataFrame({'x':x,'y':y,'z':z})
# Start with 3 clusters
kmeans = KMeans(n_clusters=4)
kmeans.fit(df)
# Start predicting clusters
labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_
# Plot the results
fig = plt.figure(figsize=(7,7))
colmap = {1: 'r', 2: 'g', 3: 'b', 4: 'black'}
colors = list(map(lambda n: colmap[n+1], labels))
ax = Axes3D(fig)
ax.scatter(df['x'], df['y'], df['z'], color=colors)
for idx, centroid in enumerate(centroids):
  ax.scatter(*centroid, color=colmap[idx+1])
plt.show()