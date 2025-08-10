import matplotlib.pyplot as k
query = ['robots','arduino ','projects','drones']
values = [99,87,75,97]
k.pie(values,labels=query,autopct='%.f')
k.show()
