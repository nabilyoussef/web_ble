import asyncio
from bleak import BleakServer, BleakGATTService

# Define your GATT Service UUID and Characteristics UUID
SERVICE_UUID = "12345678-1234-5678-1234-56789abcdef0"
CHARACTERISTIC_UUID = "12345678-1234-5678-1234-56789abcdef1"

async def run_server():
    # Create GATT service and characteristic
    service = BleakGATTService(SERVICE_UUID)
    characteristic = service.add_characteristic(CHARACTERISTIC_UUID, "read")

    async with BleakServer(service) as server:
        print(f"Server running with service {SERVICE_UUID}")
        await server.start()

        while True:
            # Server runs infinitely, handling BLE connections
            await asyncio.sleep(1)

asyncio.run(run_server())
