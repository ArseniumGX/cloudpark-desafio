from json import load, dumps
from menu import pause, clear_screen

def read_configuration():
   clear_screen()
   try:
      with open("config.json", "r") as file:
         config = load(file)
         file.close()
         print("Arquivo está vazio") if not config else print(dumps(config, indent=2))
         pause()
   except FileNotFoundError:
      with open("config.json", "w") as file:
         file.write("{}")
         file.close()
         print("Arquivo não encontrado.\nArquivo criado com sucesso!\n")
         pause()
