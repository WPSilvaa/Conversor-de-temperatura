
while True:
    print("Conversor de temperatura")
    escolha = input(
        "Escolha a unidade de entrada (C para Celsius, F para Fahrenheit): ")

    print(escolha)

    if escolha == 'C':
        temperatura = float(input("Digite a temperatura em Celsius: "))
        resultado = (temperatura * 9/5) + 32
        print("A temperatura em Fahrenheit e:", resultado)

    elif escolha == 'F':
        temperatura = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = (temperatura - 32) * 5/9
        print("A temperatura em Celsius e:", resultado)

    else:
        print("Escolha invalida. Por favor, escolha 'C' ou 'F'.")

    break