import aiohttp
import asyncio
from src.Model.LookDir import LookDir
from termcolor import colored


class Requesition(LookDir):
    def __init__(self) -> None:
        super().__init__()

    async def request_GET(self, session, dir: str) -> None:
            try:
                async with session.get(f"{self.url}{dir}") as response:
                    if response.status in range(200, 399):
                        print(colored(f"URL: {self.url}/{dir.ljust(30)}\t STATUS:{response.status}", "green"))
                    else:
                        print(colored(f"URL: {self.url}/{dir.ljust(30)}\t STATUS:{response.status}", "yellow")) 
            except Exception as e:
                print("Erro em requests:\n", e)
