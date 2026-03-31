import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
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

def cadastrar_paciente(nome, idade, telefone):
    limpar_terminal()

    dadosPacientes['nome'] = nome
    dadosPacientes['idade'] = idade
    dadosPacientes['telefone'] = telefone
    pacientes.append(dadosPacientes.copy()) # verificar esse .copy()
    print()
    print('Paciente cadastrado com sucesso!')

    return True
    
def quantidade_de_pacientes():
    return len(pacientes)

def calcular_idade_media():
    idade_total = 0

    for paciente in pacientes:
        idade_total += paciente['idade']
    
    return idade_total / quantidade_de_pacientes()

def localizar_paciente_mais_velho():
    return max(pacientes, key= lambda x : x ['idade'])

def localizar_paciente_mais_novo():
    return min(pacientes, key= lambda x: x ['idade'])
     
def mostrar_estatisticas():
    limpar_terminal()

    print(f'O total de paciente para ser atendidos é {quantidade_de_pacientes()}')
    print()
    print(f'A idade média dos pacientes é: {calcular_idade_media():.2f}')
    print()
    
    mais_novo = localizar_paciente_mais_novo()
    mais_velho = localizar_paciente_mais_velho()
    print(f'O paciente mais velho é {mais_velho['nome']} com idade {mais_velho['idade']}')
    print()
    print(f'O paciente mais novo é {mais_novo['nome']} com idade {mais_novo['idade']}')
    
    return True

def buscar_paciente(nome):
    for paciente in pacientes:
        if paciente['nome'] == nome:
            return paciente
    return None

def listar_todos_pacientes():
    for paciente in pacientes:
        print(f'Nome: ({paciente['nome']}), idade: ({paciente['idade']}) e telefone: ({paciente['telefone']})')

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
    
    match escolha:

        case 1:

            nome = input('Digite o nome do paciente: ').capitalize()
            if len(nome) < 3:
                print('O nome não existe')
                continue

            try:
                idade = int(input('Digite a idade do paciente: '))
                if idade <= 0:
                    print('Idade inválida')
                    continue

                telefone = int(input('Digite o número de telefone: '))
            except ValueError:
                print('Digite apenas números')
                continue
            
            cadastrar_paciente(nome, idade, telefone)
        case 2:
            
            mostrar_estatisticas()
        case 3:
        
            limpar_terminal()

            nome_paciente_buscado = input('Digite o nome do paciente para buscar: ').capitalize()

            paciente_localizado = buscar_paciente(nome_paciente_buscado)

            if paciente_localizado == None:

                print('Paciente não foi localizado')
            else:
                print('Paciente localizado com sucesso: ')
                print()
                print(f'Nome: {paciente_localizado['nome']}')
                print(f'Idade: {paciente_localizado['idade']}')
                print(f'Telefone: {paciente_localizado['telefone']}')
        case 4:

            limpar_terminal()
            listar_todos_pacientes()           
        case 5:

            break
        case _:
            limpar_terminal()
            print('Digite uma opção valida!')