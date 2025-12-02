import asyncio

async def prod(q1):
    
    for i in range(5):
        value = f"value_{i}"
        await q1.put(value)
        print(f"prod: put {value} to q1")
        await asyncio.sleep(1)  

async def mid(q1, q2):
    while True:
        value = await q1.get()
        print(f"mid: got {value} from q1")
        await q2.put(value)
        print(f"mid: put {value} to q2")
        
        q1.task_done()

async def cons(q2):
    while True:
        value = await q2.get()
        print(f"cons: got {value} from q2")
        
        q2.task_done()

async def main():
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    producer = asyncio.create_task(prod(q1))
    middle = asyncio.create_task(mid(q1, q2))
    consumer = asyncio.create_task(cons(q2))
    
    # Ждем завершения производителя
    await producer
    
    # Ждем, пока все значения будут обработаны
    await q1.join()  # Ждем, пока q1 не станет пустой
    await q2.join()  # Ждем, пока q2 не станет пустой
    
    # Отменяем бесконечные задачи
    middle.cancel()
    consumer.cancel()
    
    # Ждем завершения отмененных задач
    try:
        await middle
    except asyncio.CancelledError:
        pass
    
    try:
        await consumer
    except asyncio.CancelledError:
        pass
    
    print("Все задачи завершены")

if __name__ == "__main__":
    asyncio.run(main())