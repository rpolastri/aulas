login = input('digite o seu usuario:')
senha = input('digite a sua senha:')
if login == 'rafaela' and senha == '12345678':
    print('cadastrado com sucesso')
else:
    print('cadastro incorreto')

filmes = input('digite um genero preferido:')
if filmes == 'terror':
    print('indicação: It a coisa')
elif filmes == 'romance':
    print('indicação: Diario de uma paixão')
elif filmes == 'ação':
    print('indicação: velozes e furiosos')

pontos = 0
resposta = input('quanto é 1+1?')
if resposta.lower() == '2':
    pontos += 10
resposta = input('quanto é 5+4?')
if resposta.lower() == '9':
    pontos += 10
resposta = input('quanto é 10+10?')
if resposta.lower() == '20':
    pontos +=10
