def is_bissextile():
    while True:
        input_user = input("Entrez une année à vérifier : ")

        try:
            year = int(input_user)
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                print("L'année est bissextile !")
            else:
                print("L'année n'est pas bissextile !")
        except ValueError:
            print("Ce n'est pas un entier!")


if __name__ == '__main__':
    is_bissextile()
