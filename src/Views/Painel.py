import pyfiglet
from termcolor import colored
from tqdm import tqdm

class Painel:
    def __init__(self) -> None:
        self.__title = pyfiglet.figlet_format("Lookdir", font="doom")
        
    def paine_views(self):
        print(colored(self.__title, "blue"))
        print(colored("\tBy:Arch_0x3f5",'cyan'))
        print(colored("\tDiscord:Arch_0x3f5",'cyan'))
        print(colored("\tGitHub:Archboot07",'cyan'))
        print(colored("\nurl: -u \\Wordlist: -w  \\Path: -p \\Metodo: -g\n",'blue'))

    

