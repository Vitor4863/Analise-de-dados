

print("===== MENU DE OPÇÕES =====")
print("2 - Comparar dois valores")
print("3 - Calcular o dobro de um valor")

opcao = int(input("Escolha uma opção: "))


match opcao:
    case 2:
        
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))

        if n1 > n2 :
                print(f"O primeiro valor ({n1}) é maior que o segundo ({n2}).")
        elif n1 > n2 :
                print(f"O segundo valor ({n2}) é maior que o primeiro ({n1}).")
        else :
                print("Os dois valores são iguais.")

    case 3:
      
        valor = float(input("Digite um valor: "))
        dobro = valor * 2
        print(f"O dobro de {valor} é {dobro}.")

    case _:
        # Caso a opção seja inválida
        print("Opção inválida! Tente novamente.")
