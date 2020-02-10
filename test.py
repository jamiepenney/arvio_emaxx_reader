import asyncio
from arvio_emaxx_reader.arvio_emaxx_reader import ArvioEmaxxReader

reader = ArvioEmaxxReader("emaxx")


async def run():
    value = await reader.battery_soc_percent()
    print(f"soc={value=}")

    value = await reader.power_used_watts()
    print(f"power_used={value=}")
    print("Done")

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
loop.close()
