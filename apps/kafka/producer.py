from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import asyncio

async def send_one():
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Produce message
        await producer.send_and_wait("testtopic", b"Super message")
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()


async def main():
    import time
    t=time.time()
    await asyncio.gather(*[send_one() for i in range(10000)])
    print(time.time()-t)
#asyncio.run(consume())

asyncio.run(main())
print('done')