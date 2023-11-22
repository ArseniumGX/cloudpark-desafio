from os import name, system

def menu():
   clear_screen()
   print("Selecione uma opção (Difite 0 ou tecle Ctrl+C para sair)")
   print('1. Ler configuração')
   print('2. Escrever configuração')

def clear_screen():
   system("cls") if name == "nt" else system("clear")

def pause():
   input("\nTecle ENTER para continuar...")
