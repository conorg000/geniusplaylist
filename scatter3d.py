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
              x=x, y=y, z=z, marker=dict(size=2, color='rgb(23,190,207)'))
clusters = dict(alphahull=7, name='y', opacity=0.1, type='mesh3d',
               x=x, y=y, z=z)
layout = dict(title='3D Clustering of My Songs', scene=dict(xaxis=dict(zeroline=False),
                                                           yaxis=dict(zeroline=False),
                                                           zaxis=dict(zeroline=False),
                                                           ))
fig = dict(data=[scatter, clusters], layout=layout)
py.iplot(fig, filename='3D Clustering of My Songs')

