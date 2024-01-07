import serial
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os

# Initialize Arduino Port
arduino_port = 'COM5'
baud = 115200
samples = 10
print_labels = False

# Create Arduino variable
ser = serial.Serial(arduino_port, baud)
ser.setDTR(False)
ser.flushInput()
ser.setDTR(True)
print("Connected to Arduino port:" + arduino_port)

# Create .csv
fileName = "accelerometer-data.csv"

counter = 0
datal = []
# Read accelerometer
# Adjust amount of readings
while len(datal) <= 1000:
    getData = str(ser.readline())
    data = getData[2:][:-6]
    datal.append(data)
    counter += 1
    if counter == 1:
        print("DROP!!!")
    else:
        pass
    # Add accelerometer data to .csv
    with open(fileName, 'w', newline='') as file:
        writer = csv.writer(file)
        # Turn accelerometer data to .csv format
        for row in datal:
            columns = [c.strip() for c in row.strip(', ').split(',')]
            writer.writerow(columns)

# Read .csv
df = pd.read_csv('accelerometer-data.csv',on_bad_lines='skip',names=["X", "Y", "Z","Seconds"])

# Eliminate overlapping data
zero = df[(df['Seconds'] == 0) | (df['Seconds'] == 4)].index[0]
df.drop(index=df.iloc[0:zero+1].index.tolist(), axis=0,inplace=True)

# Isolate Top G's
for g in df['Z']:
    if g > 10:
        print(g)
    else:
        pass

# Show Plot
plt.plot(df['Seconds'],df['Z'])
plt.xlabel('Milliseconds (ms)')
plt.ylabel("Acceleration (G's)")
plt.show()

# Delete .csv
os.remove(fileName)