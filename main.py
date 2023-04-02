import time
from datetime import date
import random
from statistics import mean 

SpikeList = []

def recordSV():
  Noise = random.randint(0,20)
  return Noise

def programCali():
  ListSV = []
  print("Program Calibration...")
  for n in range(0,100):
    SV = recordSV
    ListSV += [SV]
    time.sleep(0.1)
  ListAvg = int(sum(ListSV)) / int(len(ListSV))
  print("")
  print("Done Calibrating.")
  return ListSV, ListAvg

def checkingProgram(AvgNoiseLevel):
  for n in range(0,600):
    Noise = recordSV()
    if (Noise + 0) > AvgNoiseLevel:
      print(str(date.today()))
      with open('database.txt', 'w') as f:
        f.write(str(date.today()))
        f.write('\n')
      time.sleep(0.5)
    else:
      time.sleep(0.5)

ListSV, ListAvg = programCali()
checkingProgram(ListAvg)