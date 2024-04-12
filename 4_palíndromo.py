texto = input("Digite um texto: ")

texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")

texto_invertido = texto[::-1]

if texto == texto_invertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
