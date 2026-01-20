## dictionary
dic = {
    "harry":  "human being",
    "spoon":  "object"
}
print(dic["harry"])
## student id dictionary
dic = {
    123:  "ved",
    456:  "om",
    789:  "akshay"
}
print(dic[789])
info = {'name': 'karan', 'age':19, 'eligible':True}
# print(info)
# print(info.keys())
# print(info.values())
# for key in info.keys():
#    print(f"the value corresponding to the key {key} is {info[Key]}")
print(info.items())
for key, value in info.items():
    print(f"the value correspomding to the key {key} is {value}")