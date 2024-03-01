def calAGE():
    username = str(input("Please Enter Your Name: "))
    age = int(input("Please Enter Your Age: "))

    birth_year = 2024 - age

    print("Hi,", username)
    print("Your Birth Year is:", birth_year)

calAGE()
