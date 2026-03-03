import string
letters = string.ascii_letters
user_input = input()
start, end = user_input.split("-")
start_index = letters.index(start)
end_index = letters.index(end)
print(letters[start_index:end_index + 1])