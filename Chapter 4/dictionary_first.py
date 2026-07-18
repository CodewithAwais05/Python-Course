# dictionary is a collection of key-value pairs
# we can add any type of data in dictionary

info = {
    "name" : "Awais",
    "subject" : ["Python", "C", "C++"], # we can also make list
    "marks" : (90, 80, 70), # we can also make tuple
    "age" : 20,
    "is_Adult" : True
}
print(info["name"])
print(info["subject"])
print(info["marks"])
print(type(info))
info["name"] = "Ali"  # we can also change the value of key
print(info["name"])
info["surname"] = "Raza"   # we can also add new key-value pair in dictionary
print(info)