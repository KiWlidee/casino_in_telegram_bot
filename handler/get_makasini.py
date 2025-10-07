from random import randint

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import keyboards as kb

import user


makasini_router = Router()

@makasini_router.message(F.text == "👟 Слови макасины")
async def get_makasini(message: Message):
    await message.answer("Велкоме ту слови макасины Ислама.", reply_markup=kb.get_makasini_menu)

@makasini_router.message(F.text == "📜 Правила")
async def makasini_rules(message: Message):
    await message.answer("Игра стоит 50 лир. За победу дается 50 лир. Нужно угадать, какой макасинчик упадет.", 
                         reply_markup=kb.get_makasini_menu)

@makasini_router.message(F.text == "⬅️ Левый макасинчик")
async def makasin_left(message: Message):
    if user.minus_money(message.from_user.id) == "Деньги списаны.":
        user.how_much_u_lose(message.from_user.id, 50)
        user.minus_money(message.from_user.id)
        random = randint(1, 2)
        if random == 1:
            await message.answer("Ты проиграл.", reply_markup=kb.get_makasini_menu)
        else:
            user.how_much_u_won(message.from_user.id, 50)
            user.money_winner(message.from_user.id, 100)
            await message.answer("Ты выиграл макасины Ислама! 👟", reply_markup=kb.get_makasini_menu)
    else:
        await message.answer("Бэйби ноу мани", reply_markup=kb.casino_menu)

@makasini_router.message(F.text == "➡️ Правый макасинчик")
async def makasin_left(message: Message):
    if user.minus_money(message.from_user.id) == "Деньги списаны.":
        user.how_much_u_lose(message.from_user.id, 50)
        user.minus_money(message.from_user.id)
        random = randint(1, 2)
        if random == 1:
            await message.answer("Ты проиграл.", reply_markup=kb.get_makasini_menu)
        else:
            user.how_much_u_won(message.from_user.id, 50)
            user.money_winner(message.from_user.id, 100)
            await message.answer("Ты выиграл макасины Ислама! 👟", reply_markup=kb.get_makasini_menu)
    else:
        await message.answer("Бэйби ноу мани", reply_markup=kb.casino_menu)