from src.Views.Painel import Painel
from src.Core.Threads import Threads
import asyncio

if __name__ == "__main__":  
    painel = Painel()  
    painel.paine_views()
    thred = Threads()
    thred.set_param()  
    if not thred.url or not thred.path:
        print("Erro: URL ou caminho do wordlist não foram fornecidos.")
        exit(1)
    try:
        asyncio.run(thred.thred_request())
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
