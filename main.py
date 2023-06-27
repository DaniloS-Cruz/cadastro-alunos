"""
Programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.
"""
alunos = {}
while True:
    opcao = input("Digite a opção: [A]dicionar, [R]emover, [V]isualizar Alunos Matriculados ou [S]air: ").upper()
    if opcao not in ("A","R","V","S"):
        print("Opção Inválida! Digite a opção correta!")
    
    if opcao == "A":
        nome_aluno = input("Informe o NOME do Aluno: ")
        matricula_aluno = input("Informe a MATRÍCULA do Aluno: ")
        alunos[matricula_aluno] = nome_aluno #a matricula do aluno será a chave e o valor o nome do aluno

    elif opcao == "R":
        matricula_aluno = input("Informe a matrícula do Aluno para remover o cadastro: ")
        if matricula_aluno in alunos:
            del alunos[matricula_aluno]
            print("Cadastro removido com sucesso!")
        else:
            print("Matrícula não encontrada.")

    elif opcao == "V":
        if alunos == {}:
            print("Não há alunos matriculados!")
        else:
            print("RELAÇÃO DE ALUNOS MATRÍCULADOS:")
            for matricula, nome in alunos.items():
                print(f"Aluno: {nome} - Matrícula: {matricula}")
            print(f"Total de Alunos matriculados: {len(alunos)}")
    elif opcao == "S":
        print("Saindo...")
        break
