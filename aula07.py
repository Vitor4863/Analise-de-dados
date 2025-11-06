nome_fruta = input("Digite sua fruta: ")

match nome_fruta:
    case "Banana":
        print("Você escolheu a opção 1")
    case "Pera":
        print("Você escolheu a opção 2")
    case "Tomate":
        print("Você escolheu a opção 3")
    case _:
        print("Opção inválida!")
