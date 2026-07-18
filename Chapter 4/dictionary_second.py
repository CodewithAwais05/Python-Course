# nested dictionary

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

print(dict["marks"]["urdu"])

print(dict)