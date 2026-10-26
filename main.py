def printarTabuleiro(tab):
    for linha in tab:
        for campo in list(linha):
            print(campo, end = " | ")

tab1 = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
tab2 = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
tab3 = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

printarTabuleiro(tab1)