import string
import random
import time
import pyperclip
import os

os.system('cls' if os.name=='nt' else 'clear')
while True:
    tirt = input("Que quieres hacer?\n\na) Crear Contraseña\nb) Revisar Contraseña\n\n-x to Exit\n- ")

    if tirt == "a":
        os.system('cls' if os.name=='nt' else 'clear')
        print("\n----PASSWORD GENERATOR----\n   Created by dlordmdia\n\n")
        time.sleep(1)

        # List Generator
        letters = list(string.ascii_letters)
        digits = list(string.digits)
        symbols = list(string.punctuation)

        password = ""

        length = int(input("Cuantos digitos quieres que tenga tu nueva Contraseña? (Recomendado: 8+)\n- "))

        for i in range(length):
            charactertype = random.randint(1, 3)
            if charactertype == 1:
                password += random.choice(letters)
            elif charactertype == 2:
                password += random.choice(digits)
            else:
                password += random.choice(symbols)

        print(f"Tu contraseña es: {password}")
        passcopy = input("\nCopiar contraseña a portapapeles? (y/n): ")
        if passcopy == "y":
            pyperclip.copy(password)
            print("\nCopiado!\n")
            os.system('cls' if os.name=='nt' else 'clear')

    elif tirt == "b":
        os.system('cls' if os.name=='nt' else 'clear')
        print("\n----SAFE PASSWORD CHECKER----\n    Created by dlordmdia\n\n")
        print("Necesitas almenos 8 carácteres")
        while True:
            num_digits = 0
            password = input("-x to Leave | Pon tu Contraseña: ")
            for character in password:
                if character.isdigit():
                    num_digits += 1

            if len(password) >= 8 and num_digits >= 2:
                break

            elif password == "x":
                break

            else:
                print("\nTu contraseña no es segura.\n")
                time.sleep(0.4)
                print("Inténtalo otra vez.\n")
                time.sleep(2)
                os.system('cls' if os.name=='nt' else 'clear')

        print("\nTu contraseña es segura.\n")
        time.sleep(2)
        print("\n----SAFE PASSWORD CHECKER----\n    Created by dlordmdia\n")
        os.system('cls' if os.name=='nt' else 'clear')
    
    elif tirt == "x":
        break

print("\nGracias por usar Password Launcher!\n")