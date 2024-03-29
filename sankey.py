# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 13:03:50 2019

@author: alexander lucaci
"""

import plotly.plotly
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

data = dict(
    type='sankey',
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(
        color = "black",
        width = 0.5
      ),
      label = ["A1", "A2", "B1", "B2", "C1", "C2"],
      color = ["blue", "blue", "blue", "blue", "blue", "blue"]
    ),
    link = dict(
      source = [0,1,0,2,3,3],
      target = [2,3,3,4,4,5],
      value = [8,4,2,8,4,2]
  ))

layout =  dict(
    title = "Basic Sankey Diagram",
    font = dict(
      size = 10
    )
)

fig = dict(data=[data], layout=layout)
#iplot(fig, validate=False)

plotly.offline.plot(fig, filename="sankey.html")
