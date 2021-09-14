"""Given a Water Tank (cylindrical shape) with Height=10, radius=5. A pump having flow rate of
15m3 /min. write the program to find the status of the tank at user given time underflow,
overflow and fill """

h, r = 10, 5
t = float(input('enter time for check status of tank :- '))
rate = 15
# tank is cylindrical shape so its volume
vol = 3.14 * r * r * h
time = vol / rate
print(time)
if t > time:
    print(f'tank is overflow from {t - time} minutes')
elif t < time:
    print(f'tank is underflow\nit is full in {time - t} minutes')
else:
    print('tank is full')
