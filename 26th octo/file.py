# import csv
#
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             print(int(row[1]))
#
#

import pandas

# data = pandas.read_csv('weather_data.csv')
# temp_list = data["temp"].mean()
#
# print(temp_list)
# print(data["temp"].max())
#
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])


pandas.DataFrame