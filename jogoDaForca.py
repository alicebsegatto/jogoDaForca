import os, time
def limparTela():
    os.system("cls")
def aguarde(tempo):
    time.sleep(tempo)
def palavraOculta(palavraChave, letrasCorretas):
    palavraOculta = " "
    for letra in palavraChave:
        if letra in letrasCorretas:
           palavraOculta += letra
        else:
           palavraOculta += "*"
    return palavraOculta

def desenharForca(erros):
    if erros == 0:
        print("  +---+")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("    __|__ ")
    elif erros == 1:
        print("  +---+")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |")
        print("    __|__ ")
    elif erros == 2:
        print("  +---+")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("      |")
        print("    __|__ ")
    elif erros == 3:
        print("  +---+")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("      |")
        print("    __|__")
    elif erros == 4:
        print("  +---+")
        print("  O   |")
        print(" /|\  |")
        print("      |")
        print("      |")
        print("    __|__")
    elif erros == 5:
        print("  +---+")
        print("  O   |")
        print(" /|\  |")
        print(" /    |")
        print("      |")
        print("    __|__")
    elif erros == 6:
        print("  +---+")
        print("  O   |")
        print(" /|\  |")
        print(" / \  |")
        print("      |")
        print("    __|__")
limparTela()


def jogoForca():
   print("Bem-vindos ao Jogo da Forca!")
   nomeDesafiante = input("Insira o nome do Desafiante: ")
   nomeCompetidor = input("Insira o nome do Competidor: ")
   limparTela()

   print("Desafiante por favor insira a palavra chave e três dicas")
   limparTela()

   palavraChave = input("Insira a palavra chave: ")
   dica1 = input("Insira a Dica1: ")
   dica2 = input("Insira a Dica2: ")
   dica3 = input("Insira a Dica3: ")

   erros = 0
   letrasCorretas = []
   tentativasRestantes = 6
   dicasRestantes = 3
   limparTela()

   print(f"{nomeCompetidor} a palavra chave tem: ", '*' * len(palavraChave))

   while '*' in palavraOculta(palavraChave, letrasCorretas) and tentativasRestantes > 0:
      print("Digite (0) para jogar")
      print("Digite (1) para solicitar dica")
      opcao = input(" ")
      if opcao == "1":
         if dicasRestantes == 3:
            print(f"Dica: {dica1}")
            dicasRestantes -= 1
         elif dicasRestantes == 2:
            print(f"Dica: {dica2}")
            dicasRestantes -=1
         elif dicasRestantes == 1:
            print(f"Dica: {dica3}")
            dicasRestantes -=1
         else:
            print("Você já usou todas as dicas!")
       
      elif opcao == "0":
          letra = input("Digite uma letra: ")
          if len(letra) == 1:
             if letra in palavraChave:  
                letrasCorretas.append(letra)
                print("Palavra: ", palavraOculta(palavraChave, letrasCorretas))
                print("Você acertou uma letra!")
             if '*' not in palavraOculta(palavraChave, letrasCorretas):   
                print(f"Parabéns {nomeCompetidor}, você ganhou!")
                print("Você deseja jogar novamente (3) ou você deseja sair (4)")
                opcaoFinal = input("")
                if opcaoFinal == "3":
                    jogoForca()
                elif opcaoFinal == "4":
                    limparTela(0)
                    quit()
                else:
                    print("Opção Inválida.")
                    break
             
             elif letra not in palavraChave: 
                tentativasRestantes -= 1
                erros += 1
                print(f"Letra incorreta! Você tem mais {tentativasRestantes} tentativas restantes.")
                print(f"Total de erros: {erros}")
                desenharForca(erros)
          else:
                print("Opção Inválida. Por favor, insira apenas uma letra.")

      if tentativasRestantes == 0:
       print(f"A palavra chave era: {palavraChave}")
       print(f"Suas tentativas acabaram, você perdeu {nomeCompetidor}.")
       print(f"Parabéns {nomeDesafiante} você ganhou!")
       print("Você deseja jogar novamente (3) ou você deseja sair (4)")
       opcaoFinal = input("")
       if opcaoFinal == "3":
          jogoForca()
       elif opcaoFinal == "4":
          limparTela(0)
          quit()
       else:
          print("Opção Inválida.")
jogoForca()
