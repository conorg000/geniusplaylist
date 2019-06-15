# Gets the right auth token for accessing user's saved tracks
def lib_token(user):
  scope = 'user-library-read'
  token = util.prompt_for_user_token(user,scope,client_id='8c8415db222143a3bdfadf507b3d7a99',client_secret='6f5d6f0ca88e4f64ad22d46ef0c64bf0',redirect_uri='http://localhost/')
  return(token)