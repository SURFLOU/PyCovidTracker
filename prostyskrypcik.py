from covidtracker import CovidTracker
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mtick
from datetime import datetime, date
import numpy as np
from pandas import Timestamp

Covid = CovidTracker()

plt.rcParams['axes.grid'] = True

info = Covid.getInfoForMonths()
percentage = Covid.getPercentageIncrease()
percentageWeekWeek = Covid.getPercentageWeekWeek()
x1 = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

for i in range(len(info)):
    data = info[i][0]
    numbery1 = int(info[i][1])
    numbery2 = int(info[i][2])
    string = str(info[i][3])
    string = ''.join(string.split())
    numbery3 = int(float(string))
    numbery4 = float(percentage[i][1])
    numbery5 = float(percentageWeekWeek[i][1])
    x1.append(data)
    y1.append(numbery1)
    y2.append(numbery2)
    y3.append(numbery3)
    y4.append(numbery4)
    y5.append(numbery5)

x = [datetime.strptime(d, "%d.%m").replace(year=datetime.today().year) for d in x1]



figure, axis = plt.subplots(2,2)

axis[0, 0].plot(x1, y1, color="r")
axis[0, 0].set_title("Zarażenia")

axis[0, 1].plot(x1, y2, color="b")
axis[0, 1].set_title("Śmierci")

axis[1, 0].plot(x1, y3, color="g")
axis[1, 0].set_title("Ilość hospitalizacji")

axis[1, 1].plot(x1, y5, color="black")
axis[1, 1].set_title("Wzrost przypadków z tygodnia na tydzień")

axis[1,1].yaxis.set_major_formatter(mtick.PercentFormatter())

axis[0,0].annotate('Święto zmarłych', xy=(('2021-11-02'), 4514), xytext=(10, 10), 
textcoords='offset points', arrowprops=dict(arrowstyle='-|>'))

axis[0,1].annotate('Święto zmarłych', xy=(('2021-11-02'), 9), xytext=(15, 15), 
textcoords='offset points', arrowprops=dict(arrowstyle='-|>'))

axis[1,1].annotate('Święto zmarłych', xy=(('2021-11-02'), -26), xytext=(15, 15), 
textcoords='offset points', arrowprops=dict(arrowstyle='-|>'))


for ax in axis.flat:
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=10))


plt.suptitle('Rozwój COViD-19 w Polsce w 2021 roku')

figure.autofmt_xdate()
plt.show()


