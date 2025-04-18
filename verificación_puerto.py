try:

    puerto = int(input("Introduce el número de puerto: "))
    
    if 0 <= puerto <= 1023:
        print(f"El puerto {puerto} es un Puerto bien conocido.")
    elif 1024 <= puerto <= 49151:
        print(f"El puerto {puerto} es un Puerto registrado.")
    elif 49152 <= puerto <= 65535:
        print(f"El puerto {puerto} es un Puerto dinámico o privado.")
    else:
        print("El número ingresado no corresponde a un puerto válido (debe estar entre 0 y 65535).")

except ValueError:
    print("Entrada inválida. Debe ingresar un número entero.")