# Programa com menu de opções

print("===== MENU DE OPÇÕES =====")
print("2 - Comparar dois valores")
print("3 - Calcular o dobro de um valor")
opcao = int(input("Escolha uma opção: "))

if opcao == 2:
    # Opção 2: comparar dois valores
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))

    if num1 > num2:
        print(f"O maior valor é {num1}.")
    elif num2 > num1:
        print(f"O maior valor é {num2}.")
    else:
        print("Os dois valores são iguais.")

elif opcao == 3:
    # Opção 3: calcular o dobro
    valor = float(input("Digite um valor: "))
    dobro = valor * 2
    print(f"O dobro de {valor} é {dobro}.")

else:
    print("Opção inválida! Tente novamente.")
