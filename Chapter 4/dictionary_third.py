# dictionary methods

info = {
    "name" : "Awais",
    "subject" : ["Python", "C", "C++"],
    "marks" : {
        "urdu" : 90,
        "english" : 80,
        "math" : 70
    },
    "age" : 20,
    "is_Adult" : True
}

print(info["marks"].keys())  # to show all keys of the dictionary

print(info.values())  # to show all values of the dictionary

print(info.items())  # return all key:value pairs as a tuple

print(info.get("name"))  # to get value of a particular key

info.update({"city" : "FSD"})  # to update the dictionary by adding a key-value pair

print(info)

print(len(info))