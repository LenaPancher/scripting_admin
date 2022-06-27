
year = int(input("Entrez une année : "))

if year % 4 == 0 and year % 400 != 0 or year % 100 == 0:
    print("année bissextile")
else:
    print("année non bissextile")
