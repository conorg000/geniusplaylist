# This gets top tracks and their audio features
# Stores it in a dataframe
# Returns dataframe
def top_data(tkn):
  sp = spotipy.Spotify(auth=token)
  # Create a DF to put data in
  df = pd.DataFrame(columns=['track', 'artist', 'popularity', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
                 'liveness', 'valence', 'tempo'])
  results = sp.current_user_top_tracks(time_range=range, limit=50)
  for i, item in enumerate(results['items']):
    track = item['name']
    artist = item['artists'][0]['name']
    pop = item['popularity']
    analysis = sp.audio_features(item['id'])
    data = list(analysis[0].values())[:11]
    df.loc[i] = [track] + [artist] + [pop] + data
  return(df)