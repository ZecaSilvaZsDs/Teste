'''
    Criar uma túpla com nomes e preços de produtos e mostrar uma listagem organizada e formatada.
'''
produtos = ("Lápis", 1.75, "Borracha", 2, "Caderno", 15.9, "Estojo", 25, "Transferidor", 4.2, "Compasso", 9.99,
            "Mochila", 120.32, "Canetas", 22.3, "Livros", 349)
print(f'''{'='*30:^30}
{' LIVRARIA BOM DEUS ':-^30}
{'='*30:^30}
{' LISTA DE PREÇOS ':-^30}''')
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<21}', end='R$')
    else:
        print(f' {produtos[pos]:>6.2f}')
print('-'*30)