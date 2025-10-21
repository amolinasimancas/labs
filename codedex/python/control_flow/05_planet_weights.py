earth_weight = float(input('Hello space traveler! Insert your weight on Earth: '))
planet_number = int(input('Select your destination (1: mercury, 2: venus, 3: mars, 4: jupiter, 5: saturn, 6: uranus, 7: neptune): '))

if planet_number == 1:
    print('Your weight on mercury: ', earth_weight * 0.38)

elif planet_number == 2:
    print('Your weight on venus: ', earth_weight * 0.91)

elif planet_number == 3:
    print('Your weight on mars: ', earth_weight * 0.38)

elif planet_number == 4:
    print('Your weight on jupiter: ', earth_weight * 2.53)

elif planet_number == 5:
    print('Your weight on saturn: ', earth_weight * 1.07)

elif planet_number == 6:
    print('Your weight on uranus: ', earth_weight * 0.89)

elif planet_number == 7:
    print('Your weight on neptune: ', earth_weight * 1.14)

else:
    print('Invalid planet number')