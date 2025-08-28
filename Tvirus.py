from colorama import init, Fore, Style
import os
import sys
import pyfiglet

init()

def limpar():
    os.system("cls" if sys.platform == "win34" else "clear")
limpar()

def logo():
    print(pyfiglet.figlet_format("Tvirus"))
logo()

try:
    virus_achados = input(Fore.RED + "- Nome do arquivo: " + Style.RESET_ALL)
except KeyboardInterrupt:
    print("\n")
    print(Fore.RED+"saindo..."+Style.RESET_ALL)
    exit()
    
try:
    with open(virus_achados, "r") as file:
        conteudo = file.read()
        malwares_nomes = ["worm", "virus", "trojan", "ramsomware", "spyware", "rat", "backdoor", "criptojacking", "screenlogger", "keylogger"]
        
        achados = [nome for nome in malwares_nomes if nome in conteudo.lower()]
        
        if achados:
            print(Fore.YELLOW + f"- Malwares detectados no arquivo {virus_achados}:" + Style.RESET_ALL)
            for malwares in achados:
                print(Fore.BLUE + f"- malware: {malwares}" + Style.RESET_ALL)
        else:
            print(Fore.CYAN + f"- Nenhum malware detectado no arquivo {virus_achados}." + Style.RESET_ALL)
            
except FileNotFoundError:
    print(Fore.RED + f"- Arquivo '{virus_achados}' não encontrado." + Style.RESET_ALL)
    
except PermissionError:
    print(Fore.RED + f"- Acesso negado ao arquivo '{virus_achados}'." + Style.RESET_ALL)
    
except KeyboardInterrupt:
    print(Fore.RED + f"- você saiu" + Style.RESET_ALL)
    exit()
    
