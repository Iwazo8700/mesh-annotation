a = open("c2020.bin", "r")
i = 0;
for linha in a:
    print(linha,end="")
    i += 1
    if(i>100):
        break
a.close()
