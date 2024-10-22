import time

artigos = [
{'titulo': 'Applications of Artificial Intelligence in Academic Libraries',
'autores': ['Vijayakumar, S.','Sheshadri,K.N.'],
'data_publicacao': '16/05/2019',
'consultas': 569},
{'titulo': 'Data science in data librarianship: Core competencies of a data librarian',
'autores': ['Semeler, A. R.','Pinto, A. L.','Rozados, H. B. F.'],
'data_publicacao': '26/11/2019',
'consultas': 1004},
{'titulo': 'Data scientist: the sexiest job of the 21st century',
'autores': ['Davenport,T.H.','Patil, D J'],
'data_publicacao': '01/10/2012',
'consultas': 10231},
{'titulo': 'Bibliometria: evolução histórica e questões atuais',
'autores': ['Araújo,C.A.A.'],
'data_publicacao': '10/12/2006',
'consultas': 650}
] 

datas = sorted([time.strptime(dicionario["data_publicacao"], "%d/%m/%Y") for dicionario in artigos])

datasEmOrdem = [time.strftime("%d/%m/%Y",dataf) for dataf in datas]

newArtigo = []

for datasOrdenas in datasEmOrdem:

    for item in artigos:

        dataPubli = item["data_publicacao"]

        if datasOrdenas == dataPubli:

            newArtigo.append(item)

print(newArtigo)