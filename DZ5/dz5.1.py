import string
import keyword
name = input()
if name == "_":
    print(True)
elif not name:
    print(False)
elif name[0].isdigit():
    print(False)
elif not name.islower():
    print(False)
elif name in keyword.kwlist:
    print(False)
elif name.replace("_", "") == "" and len(name) > 1:
    print(False)
elif any(char in string.punctuation.replace("_", "") or char ==" " for char in name):
    print(False)
else:
    print(True)