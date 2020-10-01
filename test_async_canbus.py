import asyncio
import can
import os
import binascii
# os.system('sudo ip link set can0 type can bitrate 250000')
# os.system('sudo ifconfig can0 up')
def listen_sensor_arus(msg):
    """Regular callback function. Can also be a coroutine."""
    if msg.arbitration_id == 490784999:
        print(f"{msg.data}\tini sensor_arus")

def listen_batre(msg):
    if msg.arbitration_id != 490784999:
        print(f"{msg.data}\tini battery")

async def main():
    can0 = can.Bus('can0', bustype='socketcan_ctypes', receive_own_messages=False)
    reader = can.AsyncBufferedReader()
    logger = can.Logger('logfile.asc')

    listeners = [
        listen_batre,  # Callback function
        reader,         # AsyncBufferedReader() listener
        logger,          # Regular Listener object
        listen_sensor_arus
    ]
    # listeners1 = [
    #     ini_test,  # Callback function
    #     reader,         # AsyncBufferedReader() listener
    #     logger          # Regular Listener object
    # ]
    # Create Notifier with an explicit loop to use for scheduling of callbacks
    loop = asyncio.get_event_loop()
    # notifier1 = can.Notifier(can0, listeners1, loop=loop)
    notifier = can.Notifier(can0, listeners, loop=loop)
    # Start sending first message
    # can0.send(can.Message(arbitration_id=0))

    print('Bouncing 10 messages...')
    for _ in range(100000):
        # Wait for next message from AsyncBufferedReader
        msg = await reader.get_message()
        # Delay response
        # await asyncio.sleep(0.1)
        # msg.arbitration_id += 1
        # can0.send(msg)
    # Wait for last message to arrive
    await reader.get_message()
    print('Done!')

    # Clean-up
    notifier.stop()
    # notifier1.stop()
    can0.shutdown()

# Get the default event loop
loop = asyncio.get_event_loop()
# Run until main coroutine finishes
loop.run_until_complete(main())
loop.close()