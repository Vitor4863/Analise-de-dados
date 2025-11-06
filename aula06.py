nome = input("Digite seu nome ")
salario = float(input("Digite seu salario "))


if salario >= 3000:
    desconto = salario - (salario * 0.11)
elif  salario >= 2000:
    desconto = salario - (salario * 0.9)
else:
    desconto = salario - (salario * 0.8)


if salario >= 2000 :
    desconto_vale = salario * 0.06
else : desconto_vale = salario * 0.05

if salario >= 3000:
    bonus = 300
else:
    bonus = 200


if salario >= 3000:
  cargo = "Acionista"
elif salario >= 2000 :
    cargo = "Gerente"
else : 
    cargo = "Vendedor"


salario_liquido = salario - (desconto + desconto_vale) + bonus


print("ficha de funcionarios ")
print(f"Nome : {nome:.2f}")
print(f"Cargo : {cargo}")
print(f"Salario Bruto R$ : {salario}")
print(f"Desconto INSS :{desconto}")
print(f"Desconto vale trasporte $:  {desconto_vale}")
print(f"Bonus : {bonus}")
print(f"Salario Liquido: {salario_liquido}")
