# Makes a Radar Chart, visualising the audio features of a song
# Takes song title and data series as input

def createRadar(song, series):
    Attributes = ['popularity', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
                 'liveness', 'valence', 'tempo']    
    if len(series) > 12:
      data = series.tolist()[2:]
    else:
      data = series.tolist()
    data[0] = data[0]/100
    data[3] = data[3]/11
    data[4] = (data[4] + 30)/30
    data[11] = data[11]/211
    data += data [:1]
    
    angles = [n / 12 * 2 * pi for n in range(12)]
    angles += angles [:1]
    
    ax = plt.subplot(111, polar=True)
    

    plt.xticks(angles[:-1],Attributes)
    ax.plot(angles,data)
    ax.fill(angles, data, 'lightgreen', alpha=0.7)

    ax.set_title(song, pad=20)
    plt.show()