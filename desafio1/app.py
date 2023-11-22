from time import sleep
from menu import menu, clear_screen
from read_configuration import read_configuration
from write_configuration import write_configuration

def main():
   while True:
      menu()
      option_selected = input('Escolha: ')
      
      if option_selected == "1":
         read_configuration()
      elif option_selected == "2":
         write_configuration()
      elif option_selected == '0':
         clear_screen()
         print("Bye bye!")
         sleep(1)
         break
      else:
         print("Opção inválida!")
         sleep(1)

if __name__ == '__main__':
   main()