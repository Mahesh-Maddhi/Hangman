import random


def pics(chance):
    a = """
                   +---+
                       |
                       |
                       |
                      ==="""

    b = """
                   +---+
                   O   |
                       |
                       |
                      ==="""

    c = """
                   +---+
                   O   |
                   |   |
                       |
                      ==="""

    d = """
                   +---+
                   O   |
                  /|   |
                       |
                      ==="""

    e = """
                   +---+
                   O   |
                  /|\\  |
                       |
                      ==="""

    f = """
                   +---+
                   O   |
                  /|\\  |
                  /    |
                      ==="""

    g = """
                   +---+
                   O   |
                  /|\\  |
                  / \\  |
                      ==="""
    w = """
                    0
                   \\|/
                    |
                   / \\"""

    if chance == 0:
        return g
    if chance == 1:
        return f
    if chance == 2:
        return e
    if chance == 3:
        return d
    if chance == 4:
        return c
    if chance == 5:
        return b
    if chance == 6:
        return a
    if chance == 7:
        return w


def categories(num):
    fruits = ["apple", "guava", "banana", "mango", "pineapple", "orange"]
    vegetables = ["carrot", "tomato", "bitterguard, potato, cabbage, ladyfinger, brinjal"]
    mobile_brands = ["redmi", "samsung", " vivo", "apple", "motrola", "onida", "nokia"]

    if num == 1:
        print("HINT : Fruit")
        return fruits
    elif num == 2:
        print("HINT : Vegetable")
        return vegetables
    elif num == 3:
        print("HINT : Mobile Brand")
        return mobile_brands


def game():
    choice = categories(random.randint(1, 3))
    random_num = random.randint(0, len(choice) - 1)
    rand_choice = list(choice[random_num].upper())
    chances = 6
    word = []
    for i in rand_choice:
        word += "_"
        print("_", end=' ')
    print()
    while chances >= 0:
        if chances == 0:
            print(pics(chances))
            print("You have lost")
            break
        if rand_choice == ["a"] * len(word):
            print(pics(7))
            print("you have won! ")
            break
        print(f'you have {chances} chances left')
        uc = input('Guess a letter\n').upper()[0]
        if uc in rand_choice:
            for j in range(rand_choice.count(uc)):
                word[rand_choice.index(uc)] = uc
                rand_choice[rand_choice.index(uc)] = "a"
        else:
            chances -= 1
            print(pics(chances))

        for i in word:
            print(i, end=' ')
        print()


try:
    game()

except :
    print("Some thing went wrong.")
