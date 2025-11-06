preco = float(input("Digite o preço do produto"))

if preco <= 100:
    desconto = 0.10
else:
    desconto = 0;20 


valor_final = preco - (preco * desconto)

print(f"Desconto aplicado : {desconto * 100}%")
print(f"preço final com desconto : R$ {valor_final:2.f}")