import csv
import numpy as np

with open("tips.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  data_numpy = np.array(data_list)

size = data_numpy[:,6]
# print(size)
tips = np.array(data_numpy[:,1], dtype=float)
# print(tips)
bills = np.array(data_numpy[:,0], dtype=float)
# print(bills)
tip_percentages = tips/bills
# print(tip_percentages)
