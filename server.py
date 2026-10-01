import asyncio
import websockets

# Množina pro ukládání všech připojených klientů
clients = set()

async def handle_client(websocket):
    # Přidání nového klienta
    clients.add(websocket)
    client_ip = websocket.remote_address
    print(f"[+] Připojen nový klient: {client_ip}")

    try:
        # Naslouchání na příchozí zprávy
        async for message in websocket:
            print(f"[{client_ip}] Poslal: {message}")
            
            # Odpověď zpět odesílateli
            await websocket.send(f"Server přijal: {message}")

    except websockets.exceptions.ConnectionClosedError:
        pass
    finally:
        # Odebrání klienta při odpojení
        clients.remove(websocket)
        print(f"[-] Klient odpojen: {client_ip}")

async def main():
    host = "0.0.0.0"  # Pro přístup z lokální sítě změň na "0.0.0.0"
    port = 8765
    
    async with websockets.serve(handle_client, host, port):
        print(f"🚀 WebSocket server běží na ws://{host}:{port}")
        await asyncio.get_running_loop().create_future()  # Běží nepřetržitě

if __name__ == "__main__":
    asyncio.run(main())