mesh = open("c2020.bin", "r")
i = 0
for linha in mesh:
    linha = linha.split([" = ", ","])
    if(len(linha)>0 and linha[0] == "NM"):
        for a in range(1, len(linha)):
            print(linha[a])
        i+=1
    if(i>30):
        break
mesh.close()
