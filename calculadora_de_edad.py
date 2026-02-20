from datetime import date
print("#---------------------------#")
print("#--| calculadora de edad |--#")
print("#---------------------------#")
anio_nacimiento = int(input("ingrese su año de nacimiento: "))
anio_actual = date.today().year
edad = anio_actual - anio_nacimiento
print(f"su edad es: {edad} años")