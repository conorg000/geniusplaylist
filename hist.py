# Plots 12 subplots, each one a histogram of an audio feature
varlist = ['popularity', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
                 'liveness', 'valence', 'tempo']
fig = plt.figure(figsize=(20,12))
fig.subplots_adjust(wspace = 0.2, top=1)
for i in range(0, len(varlist)):
  ax = fig.add_subplot(3,4,i+1)
  ax = music[varlist[i]].plot(kind='hist', color='lightgreen', bins=50)
  ax.set_title(varlist[i])
  ax.set_xlabel('')
plt.show()