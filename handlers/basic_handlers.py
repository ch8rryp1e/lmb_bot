from aiogram import Router, types
from aiogram.filters.command import Command


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Здравствуйте!\n\n"
        "В этом тесте собраны признаки,"
        "по которым мы с коллегами можем увидеть"
        "дефицит половых гормонов у женщины.\n"
        "Речь идёт о:\n"
        "• эстрогенах\n"
        "• тестостероне\n"
        "• прогестероне\n"
        "Даже без погружения в результаты анализов."
    )
