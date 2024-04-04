import pandas as pd
import numpy as np
#objective of this code:
# find the city with the highest number of unicorns
#then find the city with the highest valuation unicorn
#then add all the valuations of the city having the most number of unicorns
# see the difference between the two
file = pd.read_csv("datasets/worldwide-unicorns.csv", usecols=['Valuation ($B)','Country'])
valuation = file['Valuation ($B)'].to_numpy()
list_of_values = []
for i in range(len(valuation)):
    values =valuation[i].split("$")
    list_of_values.append(values[1])

actual_list = []
for j in range(len(list_of_values)):
    t = float(list_of_values[j])
    actual_list.append(t)


print(actual_list)


