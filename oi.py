# from mesh import Mesh_init
#
# teste = Mesh_init()
# arq = str(input())
arq = "oioi"
vet = ""
jsonString = open(arq, "r")
for linha in jsonString:
    vet = vet + linha
vet = vet.split("\n")
# print(vet)
vet = "\", \"".join(vet)
print(vet)
# a = open("novo.txt", "w")
# a.writelines(vet)
# jsonString.close()
# a.close()
