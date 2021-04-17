import random
import numpy as nmp
import pandas as pd
import csv
import matplotlib.pyplot as plt
def grafikeng():
    highy = [0,1,1]
    highx = [5,6,7]
    lowx = [1,2,4]
    lowy = [1,1,0]
    medx = [2,4,5,6]
    medy = [0,1,1,0]
    plt.plot(highx,highy)
    plt.plot(lowx,lowy)
    plt.plot(medx,medy)
    plt.show
def grafikfoll():
    highy = [0,1,1]
    highx = [60000,65000,95000]
    lowx = [1,10000,20000]
    lowy = [1,1,0]
    medlowx = [10000,20000,25000,30000]
    medlowy = [0,1,1,0]
    medhighx = [25000,30000,60000,65000]
    medhighy = [0,1,1,0]
    plt.plot(highx,highy)
    plt.plot(lowx,lowy)
    plt.plot(medlowx,medlowy)
    plt.plot(medhighx,medhighy)
    plt.show
data = pd.read_csv("influencers.csv")
dataid = data['id']
datafollower = data['followerCount']
dataengage = data['engagementRate']
listfollow = []
listengage = []
def folren(f):
    if (f <= 10000):
        return 1
    if (f >= 10000):
        return 0
    else:
        return ((20000-f)/(20000-10000))
def folmenbaw(f):
    if ((f > 10000) and (f < 20000)):
        return ((f-20000)/(20000-10000)) 
    if ((f >= 20000) and (f <= 25000)):
        return 1
    if ((f > 25000) and (f < 30000)):
        return ((25000-f)/(30000-25000))
    else:
        return 0
def folmentas(f):
    if ((f > 25000) and (f < 30000)):
        return ((f-25000)/(30000-25000)) 
    if ((f >= 30000) and (f <= 60000)):
        return 1
    if ((f > 60000) and (f < 650000)):
        return ((60000-f)/(65000-60000))
    else:
        return 0
def folting(f):
    if (f >= 60000):
        return 1
    if (f < 60000):
        return 0
    else:
        return ((f-70000)/(75000-70000))
def eren(e):
    if (e <= 2.0):
        return 1
    if (e >=2.0):
        return 0 
    else:
        return ((2.0-e)/(4.0-2.0))
def esed(e):
    if ((e > 2.0) and (e < 4.0)):
        return ((e-2.0)/(4.0-2.0)) 
    elif ((e >= 4.0) and (e <= 5.0)):
        return 1
    elif ((e > 5.0) and (e < 6.0)):
        return ((6.0-e)/(6.0-5.0))
    else:
        return 0
def eting(e):
    if (e >= 6.0):
        return 1
    elif ((e > 5.0) and (e < 6.0)):
        return ((e-5.0)/(6.0-5.0))
    else:
        return 0
def Followers(f):
    listfollow.append([folren(f), folmenbaw(f), folmentas(f),folting(f)])
def Rate(e):
    listengage.append([eren(e), esed(e),eting(e)])
for i in range(len(dataid)):
    Followers(datafollower[i])
for i in range(len(dataid)):
    Rate(dataengage[i])
rules = []
for i in range(len(dataid)):
    rule1 = min(listfollow[i][0], listengage[i][0])
    rule2 = min(listfollow[i][1], listengage[i][0])
    rule3 = min(listfollow[i][2], listengage[i][0])
    rule4 = min(listfollow[i][3], listengage[i][0])
    rule5 = min(listfollow[i][0], listengage[i][1])
    rule6 = min(listfollow[i][1], listengage[i][1])
    rule7 = min(listfollow[i][2], listengage[i][1])
    rule8 = min(listfollow[i][3], listengage[i][1])
    rule9 = min(listfollow[i][0], listengage[i][2])
    rule10 = min(listfollow[i][1], listengage[i][2])
    rule11 = min(listfollow[i][2], listengage[i][2])
    rule11 = min(listfollow[i][3], listengage[i][2])
    rules.append([max(rule1,rule2), max(rule3, rule4), max(rule5, rule6),max(rule7, rule8),max(rule9, rule10),max(rule10, rule11)])
hasil = []
for i in range(len(rules)):
    x = 0
    y = 0
    for j in range(4):
        rdm = random.randint(0,100)
        if (rdm<=30):
            x = x + 0
            y = y + 0
        if ((rdm>=31) and (rdm<=69)):           
            x = x + (rdm * rules[i][0])
            y = y + rules[i][0]
        if (rdm>=70):
            x = x + (rdm * rules[i][2])
            y = y + rules[i][2]
    if (y == 0):
        hasil.append([i,0])
    else:
        hasil.append([x/y])

terbaik = [x for _,x in sorted(zip(hasil,dataid), reverse=True)]
terbaik[:20]
rows = zip(terbaik[:20])
with open("choosen.csv", "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
