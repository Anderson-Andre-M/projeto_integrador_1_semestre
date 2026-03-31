import os

def limpar_terminal():

    os.system('cls')
    return True

def mostrar_menu():

    print()
    print(f'{3*"-="} SISTEMA CLÍNICA VIDA+ {3 * "=-"}')
    print('1. Cadastrar paciente')
    print('2. Ver estatisticas')
    print('3. Buscar paciente')
    print('4. Listar todos os pacientes')
    print('5. Sair')
    print()

    return True

def cadastrar_paciente():

    dadosPacientes['nome'] = str(input('Digite o nome do paciente: '))
    dadosPacientes['idade'] = int(input('Digite a idade do paciente: '))
    dadosPacientes['telefone'] = int(input('Digite o número de telefone: '))
    pacientes.append(dadosPacientes.copy())
    print()
    print('Paciente cadastrado com sucesso!')

    return True
    






dadosPacientes = {}
pacientes = [{'nome': 'Anderson', 'idade': 20, 'telefone':988223359}, {'nome': 'Aissa', 'idade': 19, 'telefone':940028922}, {'nome': 'Mocinha', 'idade': 76, 'telefone':980028922}]

while True:

    escolha = 0
    
    mostrar_menu()

    try:

        escolha = int(input('Escolha uma opção: '))
        print()
    except ValueError:

        limpar_terminal()
        print("Escolha invalida, digite apenas números")
        continue
    
    # Muda as ações dependendo da escolha
    if escolha == 1:

        limpar_terminal()
        cadastrar_paciente()
    elif escolha == 2:
        idade = 0
        idadeM = 0
        
        limpar_terminal()
        # Mostra a quantidade de pacientes cadastrados
        print(f'o número total de pacientes é: {len(pacientes)}')
        print()

        # Mostra a idade média dos pacientes 
        for paciente in pacientes:
            idade += paciente['idade']
        idadeM = idade / len(pacientes)
        print(f'A idade média dos pacientes é {idadeM}')
        print()

        # Mostra o paciente mais novo cadastrado e o mais velho
        mais_velho = max(pacientes, key=lambda x: x['idade'])
        mais_novo = min(pacientes, key=lambda x: x['idade'])

        print(f'Paciente mais velho {mais_velho["nome"]},  {mais_velho["idade"]} anos')
        print(f'Paciente mais novo {mais_novo["nome"]},  {mais_novo["idade"]} anos')
        print()

    elif escolha == 3:
        
        limpar_terminal()
        busca_paciente = str(input('Digite o nome do paciente para buscar: '))
        
        for paciente in pacientes:
            if paciente['nome'] == busca_paciente:
                print()
                print(f'Paciente localizado com sucesso!')
                print()
                print(f'{3*'-'} cadastro do paciente {3*'-'}')
                print(f'Nome: {paciente["nome"]}')
                print(f'Idade: {paciente["idade"]}')
                print(f'Telefone: {paciente["telefone"]}')

    elif escolha == 4:
        limpar_terminal()
        for paciente in pacientes:
            print(f'Nome: ({paciente['nome']}), idade: ({paciente['idade']}) e telefone: ({paciente['telefone']})')
        
    elif escolha == 5:
        break
    else:
        limpar_terminal()
        print('Digite uma opção valida!')