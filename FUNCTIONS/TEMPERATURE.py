def degree_to_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 3.2
    return round(fahrenheit, 2)


print("Temperature in F ", degree_to_fahrenheit(37.2))
