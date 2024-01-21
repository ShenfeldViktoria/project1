
number = input("Введіть число: ")
try:
    number = int(number)
    if number % 3 == 0:
        print(f"{number}mogna podiliti na 3")
    else:
        print(f"{number}ne mogna podiliti na 3 bez zalishku ")
except ValueError:
    print("Vvedeno ne virne chislo ")
