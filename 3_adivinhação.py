import random
numero_secreto = random.randint(1, 10)
tentativas = 3

while tentativas > 0:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if palpite == numero_secreto:
        print("Parabéns! Você acertou.")
        break
    elif palpite < numero_secreto:
        print("Seu palpite está muito baixo.")
    else:
        print("Seu palpite está muito alto.")
    tentativas -= 1

if tentativas == 0:
    print("Suas tentativas acabaram. O número secreto era:", numero_secreto)

print("Fim do jogo.")
