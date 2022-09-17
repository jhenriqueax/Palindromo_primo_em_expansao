def palindromo(z):
    if str(z) == "".join(reversed(str(z))):
        return True

def primo(x):
    contador = 0
    for num in range(x):
        novo = num + 1
        if (x % novo == 0):
            contador += 1
    if (contador == 2):
        print(x)

with open("pi-billion.txt") as file:
    valor = ""
    ignora = ""
    ignoraNum = 0
    contador = 0
    while True:
        for line in file:
            for num in line:
                #ignora o 3.1
                if ignoraNum != 2:
                    ignora += str(num)
                    ignoraNum += 1
                else:
                    valor += str(num)
                    if len(valor) > 8:
                        if(palindromo(valor)):
                            if valor[0] != "0":
                                print(f"resultado: {valor}")
                                break
                        print(valor)
                        contador += 1
                        valor = ""



