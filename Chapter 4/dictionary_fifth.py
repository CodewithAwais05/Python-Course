dict = {
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

# print(dict["name1"]) #shows error

print(dict.get("name1")) # doesn't show error

# so we use methods to neglect small errors like above