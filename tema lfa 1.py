import csv
with open('cuvinte.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    list = [
        ['#', '1', '#', '#', '#'],
        ['#', '1', '0', '#', '#'],
        ['#', '#', '#', '2', '#'],
        ['0', '1', '#', '2', '3'],
         ['#', '#', '#', '#', '#']
            ]
    list_fin = []
    print("Introduce numarul de noduri")
    n = int(input())
    print("Introduce nodul start")
    st = int(input())
    print("Introduce numarul de noduri finale")
    fin = int(input())

    for i in range(0, fin):
        print("Introduce nod final")
        nod_fin = int(input())
        list_fin.append(nod_fin)

    for line in csv_reader:
        cuv = line
        len_cuv = len(cuv)

        if len_cuv == 0 and (st in list_fin):
            print("APARTINE LIMBAJULUI")
        else:
            j = 0
            i = st
            pos = 0  # pozitia curenta in cuvant

            while pos < len_cuv:
                if cuv[pos] in list[i][j]:
                    if pos == (len_cuv - 1):
                        if j in list_fin:
                            print("APARTINE LIMBAJULUI")
                            pos = len_cuv
                        else:
                            print("NU APARTINE LIMBAJULUI")
                            pos = len_cuv
                    else:
                        i = j
                        j = 0
                        pos += 1
                elif j == (n - 1):
                    print("NU APARTINE LIMBAJULUI")
                    pos = len_cuv
                elif j != (n - 1):
                    j += 1






























