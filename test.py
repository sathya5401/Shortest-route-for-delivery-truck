import geopy.distance
import pandas as pd
import numpy as np
from numpy import reshape
from sys import maxsize
from itertools import permutations
import csv



def readfile(filename):
    df = pd.read_csv(filename, skipinitialspace=True, usecols=["name", "latitude", "longitude"])
    print(df)
    return df

def writefile(dis0,dis1,dis2,dis3,dis4,dis5,filename):
    fields = ['Dis0', 'Dis1', 'Dis2', 'Dis3', 'Dis4', 'Dis5']
    rows = [dis0, dis1, dis2, dis3, dis4, dis5]
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

def calcdis(df,size,des):
    disfromdes=[]
    lat1 = df.iloc[des,1]
    long1= df.iloc[des,2]
    coords1=(lat1,long1)


    for i in range(size):
        if (i==des):
            dis=0
            disfromdes.append(int(dis))
            continue
        else:
            lat2 = df.iloc[i, 1]
            long2 = df.iloc[i, 2]
            coords2 = (lat2, long2)
            dis=int(geopy.distance.distance(coords1, coords2).km)
            disfromdes.append(int(dis))

    print(disfromdes)
    return disfromdes

def getDis(x,j,filename):
     df = pd.read_csv(filename, skipinitialspace=True, usecols=["Dis0","Dis1","Dis2","Dis3","Dis4","Dis5"])
     #print(df)
     #print(df.iloc[j,x])
     return df.iloc[j,x]

def getpath(source,numofvertex,filename):
    vertex = []
    for i in range(numofvertex):

        for i in range(numofvertex):
             if i != source:
                 vertex.append(i)
        min_dis = maxsize
        next_permutation = permutations(vertex)
        for i in next_permutation:
            #print(i)
            path = []
            current_dis=0
            x=source
            path.append(source)
            for j in i:
                current_dis=current_dis + getDis(x,j,filename)
                x=j
                path.append(j)
            current_dis=current_dis + getDis(x,source,filename)
            path.append(source)
            if (current_dis<min_dis):
                min_dis = current_dis
                finalpath = path
        return min_dis,finalpath


def travelling(dis0,dis1,dis2,dis3,dis4,dis5,filename):
    s=[0,1,2,3,4,5]

    for i in range(len(s)):
        source = s[i]
        output = getpath(source,len(s),filename)

    finalpath = output[1]
    print(len(finalpath))
    for i in range(len(finalpath)):
        name = df.iloc[finalpath[i],0]
        if (i+1>=len(finalpath)):
            print(name)
        else:
            print(name + " -> " , end="")


    print("\nFinal path is : " + str(output[1]) + "\n")
    print("Final distance is : " + str(output[0]) + "km\n")


#df = readfile("AE.csv")
#filename = "AEdis.csv"
#df = readfile("CA.csv")
#filename = "CAdis.csv"
#df = readfile("JP.csv")
#filename = "JPdis.csv"
#df = readfile("MY.csv")
#filename = "MYdis.csv"
df = readfile("TH.csv")
filename = "THdis.csv"


rows=len(df.index)
dis0 = calcdis(df,rows,0)
dis1 = calcdis(df,rows,1)
dis2 = calcdis(df,rows,2)
dis3 = calcdis(df,rows,3)
dis4 = calcdis(df,rows,4)
dis5 = calcdis(df,rows,5)


writefile(dis0,dis1,dis2,dis3,dis4,dis5,filename)

travelling(dis0,dis1,dis2,dis3,dis4,dis5,filename)










