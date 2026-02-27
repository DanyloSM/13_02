import string
text_1 = input("Enter a text: ")
for ch in string.punctuation:
    text_1 = text_1.replace(ch, "")
words = text_1.split()
words = [word.capitalize() for word in words]
hashtag = "#" + "".join(words)
hashtag = hashtag[:140]
print(hashtag)