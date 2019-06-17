# 3D scatter plot with plotly
# Variables are energy, valence and tempo
# Get data ready
x = np.array(music['energy'])
y = np.array(music['valence'])
z = np.array(music['tempo'])

# Plotly credentials
# You'll need my key to use this
py.tools.set_credentials_file(username='cgonthegc', api_key='*******')

# With help from plotly
scatter = dict(mode = 'markers', name = 'y', type = 'scatter3d',
              x=x, y=y, z=z, text=np.array(music['track']), marker=dict(size=2, color='rgb(0,200,0)'))
#clusters = dict(alphahull=7, name='y', opacity=0.1, type='mesh3d',
#               x=x, y=y, z=z)
layout = dict(title='3D Scatter of My Songs', scene=dict(xaxis=dict(title='energy',zeroline=False),
                                                           yaxis=dict(title='valence',zeroline=False),
                                                           zaxis=dict(title='tempo',zeroline=False),
                                                           ))
#fig = dict(data=[scatter, clusters], layout=layout)
fig = dict(data=[scatter], layout=layout)
py.iplot(fig, filename='3D Scatter of My Songs')

