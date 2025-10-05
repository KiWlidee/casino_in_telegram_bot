from time import sleep

from random import choice, randint

import keyboards as kb

import user

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command


router = Router()

casino_slots = ["🍒", "🍒", "🍒", "🍏", "🍏", "🍇", "🍓", "🍑", "💩"]


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(f"""Привет {message.from_user.full_name}! Это казиныч бот со слотами.
Валюта внутриигровая, так что не очкуй.""", reply_markup=kb.register)
    
@router.message(F.text == "✍ Зарегистрироваться / 🔑 Войти")
async def register(message: Message):
    await message.answer("Ищу вас в базе данных...", reply_markup=ReplyKeyboardRemove())
    sleep(0.5)
    if user.user_find(message.from_user.id):
        user.add_znach_table()
        user.start_username_add(message.from_user.id)
        user.start_profile_stats(message.from_user.id)
        await message.answer("✅ Вы успешно зарегистрировались!", reply_markup=kb.main_menu)
    else:
        await message.answer("🔑 Вы успешно вошли в свой аккаунт!", reply_markup=kb.main_menu)

@router.message(F.text == "➡️ Перейти в основное меню")
async def casino_menu(message: Message):
    await message.answer("Поднял бабла, стали другими дела.", reply_markup=kb.main_menu)

@router.message(F.text == "🔚 Выйти")
async def stop(message: Message):
    await start(message)

@router.message(F.text == "🪪 Профиль")
async def profile(message: Message):
    pass
    """Вывести: Баланс, колличество круток в слотах, 
       колличество сыгранных игр в dice, сколько денег проиграл/выиграл"""
    stats = user.profile_stats(message.from_user.id)
    for i in stats:
        await message.answer(i, reply_markup=kb.main_menu)

@router.message(F.text == "🎰 Крутить слоты")
async def spin_slots(message: Message):
    await message.answer("Добро пожаловать в слоты! Каждая крутка будет стоить 50 вечно зеленых."
                         , reply_markup=kb.slots)

@router.message(F.text == "⬆️ Крутим")
async def spin_slots(message: Message):
    if user.slots_spin_minus_money(message.from_user.id) == "Деньги списаны.":
        user.how_much_u_lose(message.from_user.id, 50)
        user.slots_spin_add(message.from_user.id)
        await message.answer(user.slots_spin_minus_money(message.from_user.id))
        result = ""
        for _ in range(3):
            result += choice(casino_slots)
        await message.answer(result, reply_markup=kb.slots)
        if result == casino_slots[0] * 3:
            await message.answer("Поздравляю! Вы выиграли черешню и 400 вечно зеленых")
            user.how_much_u_won(message.from_user.id, 400)
            user.money_winner(message.from_user.id, 400)
        elif result == casino_slots[3] * 3:
            await message.answer("Поздравляю! Вы выиграли яблоки зеленые и 750 вечно зеленых... яблок гренни смит")
            user.how_much_u_won(message.from_user.id, 750)
            user.money_winner(message.from_user.id, 750)
        elif result == casino_slots[-4] * 3:
            await message.answer("Поздравляю! Вы выиграли кишмиш и 1000 вечно зеленых")
            user.how_much_u_won(message.from_user.id, 1000)
            user.money_winner(message.from_user.id, 1000)
        elif result == casino_slots[-3] * 3:
            await message.answer("Поздравляю! Вы выиграли американский пирог и 1500 вечно зеленых")
            user.how_much_u_won(message.from_user.id, 1500)
            user.money_winner(message.from_user.id, 1500)
        elif result == casino_slots[-2] * 3:
            await message.answer("Поздравляю! Вы выиграли пэрсик и 2000 вечно зеленых")
            user.how_much_u_won(message.from_user.id, 2000)
            user.money_winner(message.from_user.id, 2000)
    else:
        await message.answer("Бэйби ноу мани", reply_markup=kb.casino_menu)

@router.message(F.text == "🎲 Кости")
async def dice(message: Message):
    await message.answer("Добро пожаловать в dice! Каждый бросок будет стоить 50 вечно зеленых."
                         , reply_markup=kb.dice)

@router.message(F.text == "📦 Бросаем")
async def drop_dice(message: Message):
    if user.slots_spin_minus_money(message.from_user.id) == "Деньги списаны.":
        user.how_much_u_lose(message.from_user.id, 50)
        user.dice_drop_add(message.from_user.id)
        await message.answer(user.slots_spin_minus_money(message.from_user.id), reply_markup=kb.dice_game)
    else:
        await message.answer("Бэйби ноу мани", reply_markup=kb.casino_menu) 

@router.message(F.text == "🤔 Выбор одного числа")
async def dice_choose_one(message: Message):
    await message.answer("Выбери число", reply_markup=kb.dice_number_choose)
    @router.message(F.text)
    async def choose_number(message: Message):
        if message.text == "1️⃣":
            perc_num = "1"
        elif message.text == "2️⃣":
            perc_num = "2"
        elif message.text == "3️⃣":
            perc_num = "3"
        elif message.text == "4️⃣":
            perc_num = "4"
        elif message.text == "5️⃣":
            perc_num = "5"
        elif message.text == "6️⃣":
            perc_num = "6"
        else:
            await message.answer("Ну ты тупень. Выбирай из предложенных.", reply_markup=kb.dice)
        dice_number = str(randint(1, 6))
        if perc_num == dice_number:
            user.how_much_u_won(message.from_user.id, 150)
            user.money_winner(message.from_user.id, 150)
            await message.answer("Поздравляю! Вы выиграли 150 вечно зеленых", reply_markup=kb.dice)
        else:
            await message.answer(f"Рандомным числом было - {dice_number}. Ты проиграл", reply_markup=kb.dice)

@router.message(F.text == "🤔 Выбор промежутка")
async def dice_choose_promezh(message: Message):
    await message.answer("Выбери промежуток чисел", reply_markup=kb.dice_number_choose_promezh)
    @router.message(F.text)
    async def dice_chooses_pr(message: Message):
        if message.text == "1️⃣2️⃣":
            user_promezh = "12"
        elif message.text == "3️⃣4️⃣":
            user_promezh = "34"
        elif message.text == "5️⃣6️⃣":
            user_promezh = "56"
        else:
            await message.answer("Ну ты тупень. Выбирай из предложенных.", reply_markup=kb.dice) 
        dice_number = str(randint(1, 6))
        if dice_number in user_promezh:
            user.how_much_u_won(message.from_user.id, 75)
            user.money_winner(message.from_user.id, 75)
            await message.answer("Поздравляю! Вы выиграли 75 вечно зеленых", reply_markup=kb.dice)
        else:
            await message.answer(f"Рандомным числом было - {dice_number}. Ты проиграл", reply_markup=kb.dice)