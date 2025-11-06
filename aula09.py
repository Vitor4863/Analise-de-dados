atletas = {}

nome_atleta = 'inicio'

while nome_atleta != '':
    nome_atleta = input('Atleta: ')
    if nome_atleta != '':
        saltos = []
        for i in range(0, 2):
            salto = float(input('Salto %d: ' % (i + 1)))
            saltos.append(salto)
        atletas[nome_atleta] = saltos

print('\nResultado Final')
for nome_atleta, saltos in atletas.items():
    print('Atleta: %s' % nome_atleta)
    print('Saltos:', saltos)
    print('Média dos saltos: %.2f m' % (sum(saltos) / len(saltos)))
