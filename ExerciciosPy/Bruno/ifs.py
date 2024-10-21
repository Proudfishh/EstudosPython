nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

participacaoNaAula = input('A participação na aula é boa sim ou não?: ')
participacaoNaAulaf = participacaoNaAula.upper()
print(participacaoNaAulaf)

media = (nota1 + nota2) / 2

if media >= 6:
    print('Aluno aprovado!')

if media >= 5:
    notaRecuperação = float(input('Qual a nota da recuperação?'))
    if notaRecuperação >= 6:
        print('Aluno aprovado!')
        
    if notaRecuperação >=5:
        if participacaoNaAulaf == 'SIM':
            print('Aluno aprovado!')
        else:
            print('Aluno reprovado!')
    else:
        print('Aluno reprovado!')
else:
    print('Aluno reprovado!')