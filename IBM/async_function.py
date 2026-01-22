import asyncio

async def minha_funcao():
    print('olá')
    await asyncio.sleep(2)
    print('terminou')

asyncio.run(minha_funcao())