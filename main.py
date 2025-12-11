def converter_temperatura():
    print("=== Conversor de Temperatura ===")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    
    opc = int(input("Escolha: "))
    
    if opc == 1:
        c = float(input("Temperatura em Celsius: "))
        f = c * 9/5 + 32
        print(f"{c}°C = {f}°F")
    elif opc == 2:
        f = float(input("Temperatura em Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {c}°C")
    else:
        print("Opção inválida")

converter_temperatura()
