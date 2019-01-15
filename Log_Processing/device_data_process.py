import plotly #Ploty module is used for plotting the temperature test data.
from plotly import tools
import plotly.graph_objs as go
import datetime
from plotly.graph_objs import *
import re

#open device_ST_log file
with open('sample_device.log', 'r') as f1:
    read_file = f1.read()

#Seperate out PIR, ALS and temp_humidity sensor values
pir = re.compile(r'<PDT (?P<timestamp>.+)> \[\d+\] PIR: b(?P<baseline>\d+) s(?P<signal>\d+)')
als = re.compile(r'<PDT (?P<timestamp>.+)> \[\d+\] ALS: a(?P<als>\d+)')
temp_hum = re.compile(r'<PDT (?P<timestamp>.+)> \[\d+\] TMP: t(?P<temperature>\d+) h(?P<humidity>\d+)')

#Separate empty lists are created for storing values
timestamp, base, signal = [], [], []
atimestamp, alslist = [],[]
ttimestamp, templist, humlist = [], [], []

#Store pir timestamp, base and signal in separate lists
for m in pir.findall(read_file):
    timestamp.append(m[0])
    base.append(int(m[1]))
    signal.append(int(m[2]))
#Store als timestamp and als values in separate lists
for m in als.findall(read_file):
    atimestamp.append(m[0])
    alslist.append(int(m[1]))
#Store temp_hum timestamp, temperature and humidity values in separate lists
for m in temp_hum.findall(read_file):
    ttimestamp.append(m[0])
    templist.append(int(m[1]))
    humlist.append(int(m[2]))

#PIR vs time data are plotted using trace1 and trace2
#trace1 will take x axis as pir timestamp and y axis as pir base
trace1 = go.Scatter(
                    x=timestamp,
                    y=base,
                    name = 'pir base',
                    mode='markers',
                    marker=Marker(
                                  color = 'rgba(0,128,128, .8)',
                                  #line = dict(width=1),
                                  ))

#trace2 will take x axis as pir timestamp and y axis as pir signal
trace2 = go.Scatter(
                    x=timestamp,
                    y=signal,
                    name='pir signal',
                    yaxis='y2',
                    mode='markers',
                    marker=Marker(
                                  color='rgba(255,192,203, .8)',
                                  #line=dict(
                                  #width=1,
                                  #color='rgb(0, 0, 0)')
                                  ))

#ALS vs time data are plotted using trace 3
#trace3 will take take x axis as als timestamp and y axis as als
trace3 = go.Scatter(
                    x=atimestamp,
                    y=alslist,
                    name='als',
                    yaxis='y3',
                    mode='markers',
                    marker=Marker(
                                  color='green',
                                  symbol='circle',
                                  #line = dict(width=1)
                                  ))

#Temperature, humidity vs time are plotted using trace4 and trace5
#trace4 will take x axis as temp_hum timestamp and y axis as temperature
trace4 = go.Scatter(
                    x=ttimestamp,
                    y=templist,
                    name = 'temperature',
                    mode='markers',
                    marker=Marker(
                                  color='purple',
                                  symbol='circle',
                                  #line = dict(width=1)
                                  ))

#trace5 will take x axis as temp_hum timestamp and y axis as humidity
trace5 = go.Scatter(
                    x=ttimestamp,
                    y=humlist,
                    name='humidilty',
                    yaxis='y2',
                    mode='markers',
                    marker=Marker(
                                  color='orange',
                                  symbol='circle',
                                  #line = dict(width=1)
                                  ))
#Three subplots are made. Subplot1 - PIR vs time, Subplot2 - ALS vs time, Subplot3 - TEMP-HUM vs time
fig = tools.make_subplots(rows=3, cols=1, subplot_titles=('PIR vs time', 'ALS vs time','TEMP-HUM vs time'))

#Subplot1 has trace1 and trace2
fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 1)

#Subplot2 has trace3
fig.append_trace(trace3, 2, 1)

#Subplot3 has trace4 and trace5
fig.append_trace(trace4, 3, 1)
fig.append_trace(trace5, 3, 1)

#Plot is given a title
fig['layout'].update(title='Temperature Test Data Graph')

#Offline plotting is done
plotly.offline.plot(fig)
