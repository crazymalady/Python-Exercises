import pickle
import numpy as np

#writing it to file
cities_and_times = [('Amsterdam', 'Sun', (8, 52)), ('Anchorage', 'Sat', (23, 52)), ('Ankara', 'Sun', (10, 52)), ('Athens', 'Sun', (9, 52)), ('Atlanta', 'Sun', (2, 52)), ('Auckland', 'Sun', (20, 52)), ('Barcelona', 'Sun', (8, 52)), ('Beirut', 'Sun', (9, 52)), ('Berlin', 'Sun', (8, 52)), ('Boston', 'Sun', (2, 52)), ('Brasilia', 'Sun', (5, 52)), ('Brussels', 'Sun', (8, 52)), ('Bucharest', 'Sun', (9, 52)), ('Budapest', 'Sun', (8, 52)), ('Cairo', 'Sun', (9, 52)), ('Calgary', 'Sun', (1, 52)), ('Cape Town', 'Sun', (9, 52)), ('Casablanca', 'Sun', (7, 52)), ('Chicago', 'Sun', (1, 52)), ('Columbus', 'Sun', (2, 52)), ('Copenhagen', 'Sun', (8, 52)), ('Dallas', 'Sun', (1, 52)), ('Denver', 'Sun', (1, 52)), ('Detroit', 'Sun', (2, 52)), ('Dubai', 'Sun', (11, 52)), ('Dublin', 'Sun', (7, 52)), ('Edmonton', 'Sun', (1, 52)), ('Frankfurt', 'Sun', (8, 52)), ('Halifax', 'Sun', (3, 52)), ('Helsinki', 'Sun', (9, 52))]
f = open("cities_and_times.pkl", "bw")
pickle.dump(cities_and_times, f)
f.close();

#reading it from file
f = open("cities_and_times.pkl", "br")
cities_and_times = pickle.load(f)
print(cities_and_times[:30])

time_type = np.dtype([('city', 'U30'), ('day', 'U3'), ('time', [('h', int), ('min', int)])])
times = np.array(cities_and_times, dtype=time_type)
print(times['time'])
print(times['city'])
x = times[27]
print(x[0])










#lines = open("cities_and_times.pkl","br")
#cities_and_times = pickle.load(lines)
#print(cities_and_times[:30])
#[('Amsterdam', 'Sun', (8, 52)), ('Anchorage', 'Sat', (23, 52)), ('Ankara', 'Sun', (10, 52)), ('Athens', 'Sun', (9, 52)), ('Atlanta', 'Sun', (2, 52)), ('Auckland', 'Sun', (20, 52)), ('Barcelona', 'Sun', (8, 52)), ('Beirut', 'Sun', (9, 52)), ('Berlin', 'Sun', (8, 52)), ('Boston', 'Sun', (2, 52)), ('Brasilia', 'Sun', (5, 52)), ('Brussels', 'Sun', (8, 52)), ('Bucharest', 'Sun', (9, 52)), ('Budapest', 'Sun', (8, 52)), ('Cairo', 'Sun', (9, 52)), ('Calgary', 'Sun', (1, 52)), ('Cape Town', 'Sun', (9, 52)), ('Casablanca', 'Sun', (7, 52)), ('Chicago', 'Sun', (1, 52)), ('Columbus', 'Sun', (2, 52)), ('Copenhagen', 'Sun', (8, 52)), ('Dallas', 'Sun', (1, 52)), ('Denver', 'Sun', (1, 52)), ('Detroit', 'Sun', (2, 52)), ('Dubai', 'Sun', (11, 52)), ('Dublin', 'Sun', (7, 52)), ('Edmonton', 'Sun', (1, 52)), ('Frankfurt', 'Sun', (8, 52)), ('Halifax', 'Sun', (3, 52)), ('Helsinki', 'Sun', (9, 52))]



#pickle.dump(cities, lines)
#fh = open("cities_and_times.pkl", "br") # binary read
#cities_and_times = pickle.load(fh)
#print(cities_and_times.read())

#print(cities_and_times[:30])
#print(pickle.dump(cities_and_times,fh))
#:30

# turning our data into a structured array:
#time_type = np.dtype([('city','U30'), ('day','U3'), ('time',[('h',int), (
#            'min', int)])])
#times = np.array(cities_and_times, dtype=time_type)
#print(times['time'])
#print(times['city'])
#x=times[27]
#x[0]

"""
[('Amsterdam','Sun', (8,52)),
 ('Anchorage', 'Sat', (23,52)),
 ('Ankara', 'Sun', (10,52))
]

"""