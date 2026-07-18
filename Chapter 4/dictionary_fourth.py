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

# typecasting dictionary into tuples
info_tuple = list(dict.items())
print(info_tuple[2])