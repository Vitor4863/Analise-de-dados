import pandas as pd 
import matplotlib.pyplot as plt

dados = {
    'idade' : [18 , 17 , 19],
     'altura': [1.75 , 1.78 , 1.88]
}

df = pd.DataFrame(dados)



print(df)

print(df.describe)
print(df['idade'].mean)
print(df['idade'].sum)

plt.scatter(df['idade'] , df['altura'])
plt.title("Relação entre idade e altura ")
plt.xlabel("Idade")
plt.ylabel("altura (m)")
plt.grid(True)
plt.show()



df['idade'].plot(kind='hist',bins=5,
title = "distribução das idades ",
color = "skyblue", edgecolor = 'black')
plt.show()



df.boxplot(column='altura')
plt.title("Variação da Altura ")
plt.show()