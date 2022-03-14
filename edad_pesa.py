def calcular_edad(edad):
    if edad<18:
        print("eres un adolecente")
    elif edad<25:
        print("eres un adulto joven")
    elif edad<50:
        print("eres un adulto")
    else:
        print("eres un adulto Mayor")
    return


edad=int(input("digite la edad "))
calcular_edad(edad)

def estadoPeso(peso,estatura):
    estado=""
    masaCorporal = (peso / estatura**2)
    if masaCorporal < 18.5:
        estado="bajo de peso"
    elif masaCorporal <= 24.9:
        estado="normal"
    elif masaCorporal <= 29.9:
        estado="sobrepeso"
    else:
        estado="obeso"
    return (estado)

paciente=input("\nPor favor digite su nombre: ")
peso = float(input("\nPor favor introduzca su peso: "))
estatura = float(input("\nPor favor introduzca su estatura en metros: "))
resultado=estadoPeso(peso,estatura)
if resultado=="bajo de peso":
    print(f"\n{paciente}, según su IMC usted se encuentra {(estadoPeso(peso,estatura))}.")
elif resultado=="normal":
    print(f"\n{paciente}, según su IMC usted está {(estadoPeso(peso,estatura))} o posee un peso saludable.")
elif resultado=="sobrepeso":
    print(f"\n{paciente}, según su IMC usted se encuentra en estado de {(estadoPeso(peso,estatura))}.")
else:
    print(f"\n{paciente}, según su IMC usted se encuentra {(estadoPeso(peso,estatura))}.")