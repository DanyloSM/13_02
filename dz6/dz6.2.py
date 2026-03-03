seconds = int(input("Введіть число від 0 до 8640000 :"))
days = seconds // (24 * 60 * 60)
seconds %= (24 * 60 * 60)
hours = seconds // (60 * 60)
seconds %= (60 * 60)
minutes = seconds // 60
seconds %= 60
if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in (2, 3, 4) and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"
print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")