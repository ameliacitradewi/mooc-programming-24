# write your solution here
def read_fruits():
    dicts = {}
    try:
        with open("fruits.csv") as file:
            for line in file:
                line = line.replace("\n", "")
                key, value = line.split(";")
                dicts[key] = float(value)
    except Exception:
        print("Couldn't read the file!")
    return dicts
