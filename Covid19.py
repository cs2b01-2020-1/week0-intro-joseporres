
def comparargenomas(genoma_a, genoma_b):
    num = 0
    if (len(genoma_a) > len(genoma_b)):
        mayor = genoma_a
        menor = genoma_b
    else:
        mayor = genoma_b
        menor = genoma_a

    iter = 0
    while iter < len(menor):
        if menor[iter] == mayor[iter]:
            num = num + 1
        iter = iter + 1
    rpta = round((num * 100) / len(genoma_a), 2)
    return rpta

Acopia1 = open("AY274119.txt","r")
genoma1 = str(Acopia1.read())
Acopia1.close()

Acopia2 = open("AY278488.2.txt","r")
genoma2 = str(Acopia2.read())
Acopia2.close()

Acopia3 = open("MN908947.txt","r")
genoma3 = str(Acopia3.read())
Acopia3.close()

Acopia4 = open("MN988668.txt","r")
genoma4 = str(Acopia4.read())
Acopia4.close()

Acopia5 = open("MN988669.txt","r")
genoma5 = str(Acopia5.read())
Acopia5.close()


print("         ", "genoma1", "   ", "genoma2", "   ", "genoma3", "   ", "genoma4", "   ", "genoma5", "\n")

print("genoma1", " ", comparargenomas(genoma1, genoma1), "     ", comparargenomas(genoma1, genoma2), "     ",
      comparargenomas(genoma1, genoma3), "     ", comparargenomas(genoma1, genoma4), "      ",
      comparargenomas(genoma1, genoma5))

print("genoma2", " ", comparargenomas(genoma2, genoma1), "     ", comparargenomas(genoma2, genoma2), "     ",
      comparargenomas(genoma2, genoma3), "     ", comparargenomas(genoma2, genoma4), "     ",
      comparargenomas(genoma2, genoma5))

print("genoma3", " ", comparargenomas(genoma3, genoma1), "     ", comparargenomas(genoma3, genoma2), "     ",
      comparargenomas(genoma3, genoma3), "     ", comparargenomas(genoma3, genoma4), "     ",
      comparargenomas(genoma3, genoma5))

print("genoma4", " ", comparargenomas(genoma4, genoma1), "     ", comparargenomas(genoma4, genoma2), "     ",
      comparargenomas(genoma4, genoma3), "     ", comparargenomas(genoma4, genoma4), "     ",
      comparargenomas(genoma4, genoma5))

print("genoma5", " ", comparargenomas(genoma5, genoma1), "     ", comparargenomas(genoma5, genoma2), "     ",
      comparargenomas(genoma5, genoma3), "     ", comparargenomas(genoma5, genoma4), "     ",
      comparargenomas(genoma5, genoma5))
