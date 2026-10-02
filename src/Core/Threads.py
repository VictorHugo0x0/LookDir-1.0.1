from .Requisition import Requesition
import aiohttp
import asyncio

class Threads(Requesition):
    def __init__(self, max_threads=3) -> None:
        super().__init__()
        self.set_param()
        self.max_threads = max_threads
        self.wordlist = []

    def read_arq(self):
        try:
            with open(self.path, "r+") as arq:
                self.wordlist = arq.read().splitlines()
        except FileNotFoundError:
            raise FileNotFoundError("file Not exist")

    async def thred_request(self):
        self.semaphore = asyncio.Semaphore(self.max_threads)
        self.read_arq()
        timeout = aiohttp.ClientTimeout(total=5) 
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with self.semaphore:
                tasks = []
                for dir in self.wordlist: 
                    tasks.append(self.request_GET(session, dir))
                await asyncio.gather(*tasks)
