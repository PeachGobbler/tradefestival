f = open("cityGoods.txt", "r")
cities = [] 
route = {}

# place file contents into a list
for x in f:
  cities.append(x.strip().split())
f.close()

'''
Routes all cities from surplus to shortage removing cities, 
removing any city with a relatively poorly traded surplus item.
'''
for c in cities:
  for trade in cities:
    if c[1] == trade[2]:
      if c[0] not in route:
        route[c[0]] = [trade[0]]
      else:
        route[c[0]].append(trade[0])

'''
Removes cities that end in a "dead end"; not part of loop or one-way leading to one.
'''
empty = True
while (empty):
  empty = False
  for r in route:
    for item in route[r]:
      if item not in route:
        route[r].remove(item)
    if route[r] == []:
      del route[r]
      empty = True

#write routes into two files for later mapping
f = open("cityRoutes.txt", "w")
fl = open("cityRoutes2.txt", "w")
for r in route:
  for city in route[r]:
    f.write(str(r + " " + city) + "\n")
    fl.write(str("(" + r + " > " + city + ")") + "\n")
f.close()
fl.close()
