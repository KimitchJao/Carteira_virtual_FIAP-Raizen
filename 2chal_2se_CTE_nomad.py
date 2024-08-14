#Importação de módulos
import json
import os

#Função arquivo .json
def carregar_carteira():
    if os.path.isfile('carteira.json'):
        with open('carteira.json', 'r') as file:
            return json.load(file)
    else:
        dados_iniciais = {'saldo': 100.00, 'historico': []}
        with open('carteira.json', 'w') as file:
            json.dump(dados_iniciais, file)
        return dados_iniciais

#Função salvar no arquivo .json
def salvar_carteira(carteira):
    with open('carteira.json', 'w') as file:
        json.dump(carteira, file, indent=4)

#Definição do Depósito
def add_saldo(carteira, valor):
    if valor > 0:
        carteira['saldo'] += valor
        carteira['historico'].append(("Adição de saldo", valor))
        salvar_carteira(carteira)
        print(f"\nSaldo atualizado para R$ {carteira['saldo']:.2f}")
    else:
        print("\nValor inválido. O valor deve ser maior que zero.")

#Função para exibir o histórico formatado
def exibe_historico_formatado(transacoes):
    print("\nHistórico de Transações:")
    print("{:<30} {:<15}".format("Descrição", "Valor (R$)"))
    for transacao in transacoes:
        descricao, valor = transacao
        print("{:<30} {:<15.2f}".format(descricao, valor))

#Programa Principal
cart_virt = carregar_carteira()

while True:
    menu = input("""\nBem-vindo a Carteira Virtual da Shell Box by Nomad

     Opções:
  
 1. Consultar Saldo
 2. Adicionar Saldo
 3. Realizar Pagamento
 4. Exibir Histórico de Transações
        
 0. Sair
        
 Sua Opção: """)

    if menu == '1':
        saldo = cart_virt['saldo']
        print(f"\nSaldo disponível: R$ {saldo:.2f} ")

    elif menu == '2':
        while True:
            valor = input("\nDigite o valor a ser adicionado: R$ ")
            if valor.replace('.', '', 1).isdigit():
                valor = float(valor)
                add_saldo(cart_virt, valor)
                break
            else:
                print("\nValor inválido. Por favor, insira um valor numérico válido.")

    elif menu == '3':
        while True:
            valor = input("\nDigite o valor do pagamento: R$ ")
            if valor.replace('.', '', 1).isdigit():
                valor = float(valor)
                if valor > 0:
                    if valor <= cart_virt['saldo']:
                        cart_virt['saldo'] -= valor
                        cart_virt['historico'].append(("Pagamento realizado", valor))
                        salvar_carteira(cart_virt)
                        print("\nPagamento realizado com sucesso.")
                        print(f"Valor de R$ {valor:.2f} debitado com sucesso!")
                        break
                    else:
                        print("\nSaldo insuficiente para realizar o pagamento.")
                else:
                    print("\nValor inválido. O valor deve ser maior que zero.")
            else:
                print("\nValor inválido. Por favor, insira um valor numérico válido.")

    elif menu == '4':
        exibe_historico_formatado(cart_virt['historico'])

    elif menu == '0':
        print("\nObrigado por usar a Carteira da Shell Box by Nomad. Até mais! :D")
        break

    else:
        print("\nOpção inválida. Tente novamente.")
        