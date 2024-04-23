import os


def main():


    resp = 1
    lista_funcionarios = []
    while(resp != 0 ):
        print("1-Inserir funcionário")
        print("2-Alterar funcionário")
        print("3-Excluir funcionário")
        print("4-Exibir funcionário")
        opc = int(input("Digite a opção desejada (1-4) : "))
        print("\n")
        match opc:
            case 1:
                inserir_funcionario(lista_funcionarios)
            case 2:
                cpf = input("Digite o cpf do funcionario a ser alterado : ")
                indice = buscar_funcionario(lista_funcionarios, cpf)
                if(indice != -1):
                    alterar_funcionario(lista_funcionarios,indice)
                else:
                    print("CPF inexistente")
            case 3:
                cpf = input("Digite o cpf do funcionario a ser alterado : ")
                indice = buscar_funcionario(lista_funcionarios, cpf)
                if (indice != -1):
                    excluir_funcionario(lista_funcionarios, indice)
                else:
                    print("CPF inexistente")
            case 4:
                exibir_funcioanrios(lista_funcionarios)
            case _:
                print("Opção invalida")
        print("\n")
        resp = int(input("Deseja continuar (1-SIM/0-NÃO) : "))
        print("\n")

def inserir_funcionario(lista_funcionarios):
    try:
        nome = input("Digite o nome do funcionário: ")
        cpf = input("Digite o cpf do funcionário: ")
        dia = int(input("Digite o dia de nascimento: "))
        mes = int(input("Digite o mês de nascimento: "))
        ano = int(input("Digite o ano de nascimento: "))
        data_nascimento = [dia, mes, ano]
        cargo = input("Digite o cargo do funcionário: ")
        salario_bruto = float(input("Digite o salário bruto do funcionário: "))
        desconto_INSS = salario_bruto * 0.15
        desconto_IR = salario_bruto * 0.1895
        salario_liquido = salario_bruto - desconto_INSS - desconto_IR
    except ValueError:
        print("Digite valores númericos")
    else:
        funcionario={'Nome':nome,'CPF':cpf,'Data_nasc':data_nascimento,'Cargo':cargo,'Salario_bruto':salario_bruto,'Desc_INSS':desconto_INSS,'Desc_IR':desconto_IR,'salario_liquido':salario_liquido}
        lista_funcionarios.append(funcionario)
    finally:
        print("Operação finalizada")
        print("\n")
def buscar_funcionario(lista_funcionarios, cpf):
    indice = -1
    for i in range(len(lista_funcionarios)):
        if(lista_funcionarios[i]['CPF'] == cpf):
            indice = i
    return (indice)


def alterar_funcionario(lista_funcionarios, indice):
    try:
        print(f"Nome: {lista_funcionarios[indice]['Nome']}")
        nome = input("Digite o novo nome do funcionário: ")
        print(f"Dia de nascimento: {lista_funcionarios[indice]['Data_nasc'][0]}")
        dia = int(input("Digite o novo dia de nascimento: "))
        print(f"Mês de nascimento: {lista_funcionarios[indice]['Data_nasc'][1]}")
        mes = int(input("Digite o novo mês de nascimento: "))
        print(f"Ano de nascimento: {lista_funcionarios[indice]['Data_nasc'][2]}")
        ano = int(input("Digite o novo ano de nascimento: "))
        data_nascimento = [dia, mes, ano]
        print(f"Cargo: {lista_funcionarios[indice]['Cargo']}")
        cargo = input("Digite o novo cargo do funcionário: ")
        print(f"Salário bruto: {lista_funcionarios[indice]['Salario_bruto']}")
        salario_bruto = float(input("Digite o novo salário bruto do funcionário: "))
        desconto_INSS = salario_bruto * 0.15
        desconto_IR = salario_bruto * 0.1895
        salario_liquido = salario_bruto - desconto_INSS - desconto_IR
    except ValueError:
        print("Digite valores númericos")
    else:
        lista_funcionarios[indice]['Nome'] = nome
        lista_funcionarios[indice]['Cargo'] = cargo
        lista_funcionarios[indice]['Data_nasc'] = data_nascimento
        lista_funcionarios[indice]['Salario_bruto'] = salario_bruto
        lista_funcionarios[indice]['Desc_INSS'] = desconto_INSS
        lista_funcionarios[indice]['Desc_IR'] = desconto_IR
        lista_funcionarios[indice]['Salario_liquido'] = salario_liquido
        print("Funcionário alterado com sucesso!")
    finally:
        print("\n")
        print("Operação finalizada")

def excluir_funcionario(lista_funcioanrios, indice):
    lista_funcioanrios.pop(indice)
    print("Funcionário excluído com suceso")

def exibir_funcioanrios(lista_funcionarios):
    for i in range(len(lista_funcionarios)):
        print(f"FUNCIONARIO {i + 1}")
        for chave, valor in lista_funcionarios[i].items():
            print(f"{chave}: {valor}")
        print("----------------------------------------------")

if __name__ == "__main__":
    main()