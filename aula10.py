idade = int(input("Idade: "))


match idade : 

    case _ if idade < 12:
        print("Criança")
    case _ if idade < 18 :
      print("Adolescente")
    case _ if idade < 60 :
      print("Adulto")
    case _ if idade >= 60 :
       print("Melhor Idade")
    case _ :
        print("Idade invalida")