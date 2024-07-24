# Write your solution here
def histogram(s: str):
    dicts = {}
    for char in s:
        if char in dicts:
            dicts[char] += 1
        else:
            dicts[char] = 1

    for letter, count in sorted(dicts.items()):
        print(f"{letter} {'*' * count}")