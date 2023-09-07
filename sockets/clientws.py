import asyncio
import websockets #pip install websockets
import subprocess

async def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return output
    except Exception as e:
        return str(e)

async def echo(websocket, path):
    async for message in websocket:
        print(message)
        if message.lower() == 'exit':
            await websocket.close()
            return
        response = await execute_command(message)
        await websocket.send(response)

start_server = websockets.serve(echo, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()