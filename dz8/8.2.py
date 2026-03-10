def is_palindrome(text):
    clean = ""
    for char in text:
        if char.isalnum():
            clean += char
    clean = clean.lower()
    return clean == clean[::-1]
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")