# Capítulo 5/6
# Visualización de datos

# Código de ejemplo para el gráfico anterior

import pandas as pd
import numpy as np
import plotly.express as px

cases = [33, 61, 86, 112, 116, 129, 192, 174, 344, 304, 327, 246, 320, 339, 376]

dates = ['March<br>'] * len(cases)
day = 18
for i in range(len(dates)):
    dates[i] = dates[i] + str(day)
    day = day + 1
dates[-1] = 'April<br>1'

labels = dict(date="Date", cases="Number of cases")
markers = dict(size=30, line=dict(width=2, color='black'), color='white')
title = dict(text='New Cases Per Day', font=dict(color='white', size=30))
yaxis = dict(tickmode='linear', tick0=30, dtick=30)

df = pd.DataFrame({'cases': cases, 'date': dates})

fig = px.line(df, y='cases', x='date', text='cases', markers=True, labels=labels, title="New Cases Per Day")

fig.update_xaxes(showgrid=False, color='white', tickangle=0)
fig.update_yaxes(color='white', gridcolor='#5c5a5c', gridwidth=2, range=[15, 400])
fig.update_traces(marker=markers, line_color='white', line_width=6)
fig.update_layout(title=title,
                  title_x=0.5,
                  paper_bgcolor='#070230',
                  plot_bgcolor='#070230',
                  yaxis=yaxis,
                  xaxis_type='category')
fig.add_annotation(text='TOTAL CASES', 
                    align='right',
                    showarrow=False,
                    font=dict(color='white', size=12),
                    xref='paper',
                    yref='paper',
                    x=1.08,
                    y=1.25)
fig.add_annotation(text='3,342', 
                    align='right',
                    showarrow=False,
                    font=dict(color='white', size=23),
                    xref='paper',
                    yref='paper',
                    x=1.071,
                    y=1.2)

fig.show()


import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.write_html('first_figure.html', auto_open=True)



# Fin.