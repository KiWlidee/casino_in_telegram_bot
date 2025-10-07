from random import randint, uniform

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import keyboards as kb

import user 

crash_router = Router()

class Choose_cef(StatesGroup):
    waiting_number = State()

@crash_router.message(F.text == "📈 Краш")
async def crash(message: Message):
    await message.answer("Добро пожаловать в краш. Каждая игра обойдется в 50 вечно зеленых."
                         , reply_markup=kb.crash)

@crash_router.message(F.text == "📉 Играем")
async def crash_game(message: Message, state: FSMContext):
    await message.answer("Выбирайте ставку", reply_markup=kb.crash_game)
    await state.set_state(Choose_cef.waiting_number)

@crash_router.message(Choose_cef.waiting_number)
async def choose_cef_(message: Message, state: FSMContext):
    if user.minus_money(message.from_user.id) == "Деньги списаны.":
        user.how_much_u_lose(message.from_user.id, 50)
        user.minus_money(message.from_user.id)
        kef = message.text
        try:
            kef = float(kef)
            true_numbers = {1.1, 1.25, 1.4, 1.5, 1.75, 2, 2.5, 3.5, 5, 7.5, 10, 15, 25, 40}
            if kef in true_numbers:
                zero = randint(1, 100)
                if zero >= 97:
                    user.how_much_u_lose(message.from_user.id, 50)
                    user.minus_money(message.from_user.id)
                    await message.answer(f"Вы проиграли! Краш - 0.00", reply_markup=kb.crash)
                    await state.clear()
                else:
                    winner = kef * 50
                    x = randint(1, 2)
                    x2 = randint(1, 100)
                    if x == 1 and x2 <= 55:
                        crash_kef = float(str(uniform(1, 1.5))[:4])
                        if kef > crash_kef:
                            user.how_much_u_lose(message.from_user.id, 50)
                            user.minus_money(message.from_user.id)
                            await message.answer(f"Вы програли! Краш - {crash_kef}", reply_markup=kb.crash)
                            await state.clear()
                        else:
                            user.how_much_u_won(message.from_user.id, winner)
                            user.money_winner(message.from_user.id, winner)
                            await message.answer(f"Вы выиграли {winner}! Краш - {crash_kef}", reply_markup=kb.crash)
                            await state.clear()
                    elif x2 >= 55:
                        crash_kef = float(str(uniform(1.5, 2))[:4])
                        if kef > crash_kef:
                            user.how_much_u_lose(message.from_user.id, 50)
                            user.minus_money(message.from_user.id)
                            await message.answer(f"Вы програли! Краш - {crash_kef}", reply_markup=kb.crash)
                            await state.clear()
                        else:
                            user.how_much_u_won(message.from_user.id, winner)
                            user.money_winner(message.from_user.id, winner)
                            await message.answer(f"Вы выиграли {winner}! Краш - {crash_kef}", reply_markup=kb.crash)
                            await state.clear()
                    elif x2 >= 82:
                        crash_kef = float(str(uniform(2, 5))[:4])
                        if kef > crash_kef:
                            user.how_much_u_lose(message.from_user.id, 50)
                            user.minus_money(message.from_user.id)
                            await message.answer(f"Вы програли! Краш - {crash_kef}", reply_markup=kb.crash)
                            await state.clear()
                        else:
                            user.how_much_u_won(message.from_user.id, winner)
                            user.money_winner(message.from_user.id, winner)
                            await message.answer(f"Вы выиграли {winner}! Краш - {crash_kef}", reply_markup=kb.crash)
                            await state.clear()
                    elif x2 >= 95:
                        crash_kef = float(str(uniform(5, 25))[:4])
                        if kef > crash_kef:
                            user.how_much_u_lose(message.from_user.id, 50)
                            user.minus_money(message.from_user.id)
                            await message.answer(f"Вы програли! Краш - {crash_kef}", reply_markup=kb.crash)
                            await state.clear()
                        else:
                            user.how_much_u_won(message.from_user.id, winner)
                            user.money_winner(message.from_user.id, winner)
                            await message.answer(f"Вы выиграли {winner}! Краш - {crash_kef}", reply_markup=kb.crash)
                            await state.clear()
                    elif x2 >= 98:
                        crash_kef = float(str(uniform(25, 50))[:4])
                        if kef > crash_kef:
                            user.how_much_u_lose(message.from_user.id, 50)
                            user.minus_money(message.from_user.id)
                            await message.answer(f"Вы програли! Краш - {crash_kef}", reply_markup=kb.crash)
                            await state.clear()
                        else:
                            user.how_much_u_won(message.from_user.id, winner)
                            user.money_winner(message.from_user.id, winner)
                            await message.answer(f"Вы выиграли {winner}! Краш - {crash_kef}", reply_markup=kb.crash)
                            await state.clear()
                await state.clear()
            else:
                await message.answer("Еблан.", reply_markup=kb.crash)
                await state.clear()
        except ValueError:
            await message.answer("Еблан.", reply_markup=kb.crash)
            await state.clear()
    else:
        await message.answer("Бэйби ноу мани", reply_markup=kb.casino_menu)
        await state.clear()