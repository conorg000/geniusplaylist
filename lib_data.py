# Get all library data
def lib_data(tkn):
  sp = spotipy.Spotify(auth=token)
  # Create a DF to put data in
  df = pd.DataFrame(columns=['track', 'artist', 'popularity', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',
                 'liveness', 'valence', 'tempo'])
  results = sp.current_user_saved_tracks(limit=50)
  for i, obj in enumerate(results['items']):
    item = obj['track']
    track = item['name']
    artist = item['artists'][0]['name']
    pop = item['popularity']
    analysis = sp.audio_features(item['id'])
    data = list(analysis[0].values())[:11]
    df.loc[i] = [track] + [artist] + [pop] + data
  return(df)