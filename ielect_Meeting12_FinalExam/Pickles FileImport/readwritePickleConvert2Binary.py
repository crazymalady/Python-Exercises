import pickle

cities = ["Paris", "Dijon", "Lyon", "Strasbourg"]
fh = open("data.pkl", "bw")
pickle.dump(cities, fh)
fh.close()

f = open("data.pkl", "rb")
villes = pickle.load(f)
print(villes)

