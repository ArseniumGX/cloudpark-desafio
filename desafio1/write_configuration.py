from json import dump
from menu import clear_screen, pause
from re import match

def write_configuration():
   clear_screen()
   ip_format = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){2}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
   server_name = input("Informe o nome do servidor: ")
   server_ip = input("Informe o IP do servidor: ")
   while True:
      if match(ip_format, server_ip):
         break
      else:
         print("IP inválido!")
         server_ip = input("Informe o IP do servidor: ")

   server_password = input("Informe a senha do servidor: ")

   data = {
      'server_name': server_name,
      'server_ip': server_ip,
      'server_password': server_password
   }

   with open("config.json", "w") as file:
      dump(data, file)
      file.close()
      print("\nConfigurações salvas com sucesso!")
      pause()