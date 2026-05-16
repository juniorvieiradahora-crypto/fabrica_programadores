# Autor: adriano viera
# projeto: condicionais

# definiçoes das variaveis
nome = input('digite seu nome:')
idade = input('digite sua idade:')
cidade = input('digite sua cidade:')

carteira = input("voce possui carteira de motorista?(sim ou nao):")

if carteira == "sim":
    print('voce possui carteira de motorista entao pode dirigir')
else:
    print('voce nao possui carteira de motorista, nao tente')