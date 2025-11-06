numero = int(input("Digite um número: "))

match numero % 2:
    case 0:
        print(f"O número é {numero} par")
    case 1:
        print(f"O número é {numero} ímpar.")




match numero :
    case _ if numero % 2 == 0 :
      print(f" O numero {numero}","Par")

    case _:
      print (f"O numero {numero}" , "impar")