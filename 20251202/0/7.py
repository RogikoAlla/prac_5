import asyncio

async def snd(event):
    await.async.sleep(0.5)
    print(event)
    
async def mid(ev_snd, ev_mid, k):
    print(f"mid({k}): event")
    await ev_snd.wait()
    print(f"mid({k}): evsnd")
    ev_mid.set()
    print(f"mid({k}): generated evmid{k}")
    

async def rcv(ev_mid0, ev_mid1):
    """Ожидает evmid0, а затем evmid1"""
    print(f"rcv: waiting for evmid0")
    await ev_mid0.wait()
    print(f"rcv: received evmid0")
    
    print(f"rcv: waiting for evmid1")
    await ev_mid1.wait()
    print(f"rcv: received evmid1")

async def main():
    # Создаем события
    ev_snd = asyncio.Event()
    ev_mid0 = asyncio.Event()
    ev_mid1 = asyncio.Event()
    
    # Создаем задачи в указанном порядке
    tasks = [
        asyncio.create_task(rcv(ev_mid0, ev_mid1)),
        asyncio.create_task(mid(ev_snd, ev_mid1, 1)),
        asyncio.create_task(mid(ev_snd, ev_mid0, 0)),
        asyncio.create_task(snd(ev_snd))
    ]
    
    # Ждем завершения всех задач
    await asyncio.gather(*tasks)
    print("Все события обработаны")

if __name__ == "__main__":
    asyncio.run(main())

