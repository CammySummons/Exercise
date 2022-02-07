bicycling = int(input("Number of hours spent bicycling: "))
jogging = int(input("Number of hours spent jogging: "))
swimming = int(input("Number of hours spent swimming: "))

calories = bicycling*200 + jogging*475 + swimming*275
kilograms = (calories/(3500/454))/1000

print(calories)
print(kilograms)
    
