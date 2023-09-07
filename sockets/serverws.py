import asyncio
import websockets
async def connect_to_server():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            message = input("Escribe un mensaje (o 'exit' para salir): ")
            if message.lower() == 'exit':
                break
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Respuesta del servidor: {response}")

asyncio.get_event_loop().run_until_complete(connect_to_server())
