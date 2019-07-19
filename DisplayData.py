import matplotlib.pyplot as pyplot
import csv
name=[]
Configuration=[]
Production=[]
stroke=[]
bore=[]
Compression_ratio=[]
Displacement=[]
HP=[]
Torque=[]
Redline=[]

with open("database.csv") as csvfile:
    plots = csv.reader(csvfile,delimiter=',')
    for column in plots:
        print("i")
data_file = np.loadtxt()