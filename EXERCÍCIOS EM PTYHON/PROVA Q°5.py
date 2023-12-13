matriz = [[0] * 8 for _ in range(4)]

def dados_usuário():

    alunos = []
    Q_comp = 0
    Q_infor = 0
    Q_redes = 0

    alunos_aprovados = 0
    alunos_reprovados = 0
    nome_do_aluno = ""

    maior_nota = 0

    for _ in range(7):
        nome = input('Nome: ')
        nota = float(input("Nota: "))
        curso = input("Curso (Computação, informática ou redes): ").lower()
        if 7 <= nota <= 10:
            situação = "Aprovado"
            alunos_aprovados += 1
        else:
            situação = "Reprovado"
            alunos_reprovados += 1
        
        if nota > maior_nota:
            maior_nota = nota
            nome_do_aluno = nome

        if curso == "computação": 
            Q_comp += 1
        elif curso == "informática":
            Q_infor += 1
        elif curso == "redes":
            Q_redes += 1

        
        print("-=" * 32)
        alunos.append([nome, nota, curso, situação])



    return alunos, Q_comp, Q_infor, Q_redes, alunos_aprovados, alunos_reprovados, maior_nota, nome_do_aluno



def organização(alunos):
    tabela = [["Nome", "Nota", "Curso", "Situação" ]] + alunos

    média_geral = tabela[1][1] + tabela[2][1] + tabela[3][1] + tabela[4][1] + tabela[5][1] + tabela[6][1] + tabela[7][1] 

    return tabela, média_geral



def main():
    alunos, Q_comp, Q_infor, Q_redes, alunos_aprovados, alunos_reprovados, maior_nota, nome_do_aluno = dados_usuário()
    tabela, média_geral = organização(alunos)

    for linha in tabela:
        print("{:<20} {:<10} {:<20} {:<10}".format(*linha))

    print("-="*32)

    print(f"\nMédia geral da turma é {média_geral:.2f}.")

    print(f"\nA quantidade de alunos de cada curso é {Q_comp} para a computação, {Q_infor} para a informática e {Q_redes} para redes.")

    print(f"\nPercentual de alunos aprovados são {alunos_aprovados / len(alunos) * 100:.2f}% e reprovados {alunos_reprovados / len(alunos) * 100:.2f}%.")

    print(f"\nAluno com maior nota foi {nome_do_aluno} com nota {maior_nota}.")

if __name__ == "__main__":
    main()