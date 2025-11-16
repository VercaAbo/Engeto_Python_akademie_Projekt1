TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

pocet_textu = len(TEXTS)

pristupy = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("username: ")
password = input("password: ")

if username in pristupy and pristupy[username] == password:
    print("Welcome to the app, " + username)
    print("We have " + str(pocet_textu) + " texts to be analyzed.")
else:
    print("Unregistered user, terminating the program.")
    quit()

vybrany_text = input("Enter a number btw. 1 and " + str(pocet_textu) +
                     " to select: ")

if not vybrany_text.isnumeric():
    print("Invalid value.")
    quit()
elif int(vybrany_text) > pocet_textu or int(vybrany_text) < 1:
    print("Invalid value.")
    quit()
else:
    surova_slova = TEXTS[int(vybrany_text)-1].split()

    vycistena_slova = []

    for slovo in surova_slova:
        ocistene_slovo = slovo.strip('.,;:!?()[]{}"\'')
        vycistena_slova.append(ocistene_slovo)

    pocet_slov = len(vycistena_slova)

    pocet_velkych_zac = 0
    for slovo in vycistena_slova:
        if slovo.istitle():
            pocet_velkych_zac = pocet_velkych_zac + 1

    pocet_velkych = 0
    for slovo in vycistena_slova:
        if slovo.isupper():
            pocet_velkych = pocet_velkych + 1

    pocet_malych = 0
    for slovo in vycistena_slova:
        if slovo.islower():
            pocet_malych = pocet_malych + 1

    pocet_cisel = 0
    soucet_cisel = 0
    for slovo in vycistena_slova:
        if slovo.isnumeric():
            pocet_cisel = pocet_cisel + 1
            soucet_cisel = soucet_cisel + int(slovo)

    vyskyt_delek_slov = {}

    for slovo in vycistena_slova:
        if len(slovo) in vyskyt_delek_slov:
            vyskyt_delek_slov[len(slovo)] += 1
        else:
            vyskyt_delek_slov[len(slovo)] = 1

    print("There are " + str(pocet_slov) + " words in the selected text.")
    print("There are " + str(pocet_velkych_zac) + " titlecase words.")
    print("There are " + str(pocet_velkych) + " uppercase words.")
    print("There are " + str(pocet_malych) + " lowercase words.")
    print("There are " + str(pocet_cisel) + " numeric strings.")
    print("The sum of all the numbers is " + str(soucet_cisel) + ".")
    print("-" * 40)
    print("LEN|          OCCURRENCES          |NR.")
    print("-" * 40)

    for delka in sorted(vyskyt_delek_slov.keys()):
        print(
            f"{delka:<3}| {'*' * vyskyt_delek_slov[delka]:<29} | " + 
            f"{vyskyt_delek_slov[delka]}")
