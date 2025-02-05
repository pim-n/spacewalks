import csv
import datetime as dt
import json

import matplotlib.pyplot as plt

# https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r')
output_file = open('./eva-data.csv','w')
graph_file = './cululative_ev_graph.png'

fieldnames = ("EVA #", "Country", "Crew    ", "Vehicle", "Date", "Duration", "Purpose")

data=[]

for i in range(374):
    line=input_file.readline()
    print(line)
    data.append(json.loads(line[1:-1]))
#data.pop(0)
## Comment out this bit if you don't want the spreadsheet

w=csv.writer(output_file)

time = []
date =[]

j=0
for i in data:
    print(data[j])
    # and this bit
    w.writerow(data[j].values())
    if 'duration' in data[j].keys():
        eva_duration_str = data[j]['duration']
        if eva_duration_str == '':
            pass
        else:
            eva_duration = dt.datetime.strptime(eva_duration_str,'%H:%M')
            eva_total_hours = dt.timedelta(hours=eva_duration.hour, minutes=eva_duration.minute, seconds=eva_duration.second).total_seconds()/(60*60)
            print(eva_duration, eva_total_hours)
            time.append(eva_total_hours)
            if 'date' in data[j].keys():
                date.append(dt.datetime.strptime(data[j]['date'][0:10], '%Y-%m-%d'))
                #date.append(data[j]['date'][0:10])

            else:
                time.pop(0)
    j+=1

t=[0]
for i in time:
    t.append(t[-1]+i)

date,time = zip(*sorted(zip(date, time)))

plt.plot(date,t[1:], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
