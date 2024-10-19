nome='maria'
idade='20'
altura=1.70
isAtivo=True

frutas = {'banana', 'maça', 'pêra'}
for fruta in frutas:
    print(fruta)

pessoa = {
    'nome': 'maria',
    'idade': 20,
    'altura':1.70,
    'isAtivo': False
}

pessoa.get('nome')
pessoa.pop('isAtivo')

# and or not && || !
if idade > 18:
    print('maior de idade')
    pass
elif idade == 18:
    print('Tem 18 anos')
else:
    print('menor de idade')

def soma(a,b):
    print('somando...')
    return a+b

print(soma(2,3))







