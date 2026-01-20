## union
s1 = {1,2,3,4}
s2 = {4,7,3,8}
print(s1.union(s2))
s1.update(s2)
# s2.update(s1)
print(s1,s2)
## unoin
cities1 = {"tokyo","madrid","berlin","delhi"}
cities2 = {"tokyo","seoul","kabul","madrid"}
cities3 = cities1.union(cities2)
print(cities3)
## intersection
cities1 = {"tokyo","madrid","berlin","delhi"}
cities2 = {"tokyo","seoul","kabul","madrid"}
cities3 = cities1.intersection(cities2)
print(cities3)
## intersection update
cities = {"tokyo","madrid","berlin","delhi"}
cities2 = {"tokyo","seoul","kabul","madrid"}
cities3 = cities.difference(cities2)
print(cities3)
## superset
cities = {"tokyo","madrid","berlin","delhi"}
cities2 = {"seoul","kabul"}
print(cities.issuperset(cities2))
cities3 = {"tokyo", "madrid", "delhi"}
print(cities.issuperset(cities3))
print(cities.issubset(cities))
## pop
## pop means remove
cities = {"tokyo", "madrid", "berlin", "delhi"}
item = cities.pop()
print(cities)
print(item)