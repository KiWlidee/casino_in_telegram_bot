import os

from time import sleep

from random import choice, randint

import keyboards as kb

import user

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, BufferedInputFile
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


router = Router()

casino_slots = ["🍒", "🍒", "🍒", "🍏", "🍏", "🍇", "🍓", "🍑", "💩"]

#  blackjack = [2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 
# 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]

class Admin_enter_to_panel(StatesGroup):
    waiting_number = State()

class Admin_change_money(StatesGroup):
    waiting_number = State()

class Admin_finder_people(StatesGroup):
    waiting_number = State()

class RouletteStates_one(StatesGroup):
    waiting_number = State()

class RouletteStates_two_color(StatesGroup):
    waiting_number = State()

class DiceStates_one(StatesGroup):
    waiting_number = State()

class DiceStates_many(StatesGroup):
    waiting_number = State()

YOUR_USER_ID = 1414872963

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(f"""Привет {message.from_user.full_name}! Это казиныч со слотами.
Валюта внутриигровая, так что не очкуй.
Но есть бабки закончатся, то нужно будет жестко депать, или просить денюжки у Админа.""", reply_markup=kb.register)
    
    
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

@router.message(F.text == "🛠️")
async def admin_panel(message: Message, state: FSMContext):
    await message.answer("Это - Админ панель, сюда не суйся.")
    await state.set_state(Admin_enter_to_panel.waiting_number)

@router.message(Admin_enter_to_panel.waiting_number)
async def process_admin_password(message: Message, state: FSMContext):
    if message.text == "14881777":
        if user.user_check(message.from_user.id):
            random_money = randint(40000, 75000)
            user.money_winner(message.from_user.id, random_money)
            await message.answer(f"Промокод засчитан! На баланс было добавлено {random_money}. \
                                Перейдите в профиль, чтобы проверить баланс", 
                                reply_markup=kb.ADMIN_panel)
            await state.clear()
        else:
            user.money_winner(message.from_user.id, -10000)
            await state.clear()
            await message.answer("За такие фокусы, я забираю у тебя 10000")
            await start(message)
    elif message.text == "8038":
        await message.answer("Привет, Админ!", reply_markup=kb.ADMIN_panel)
        await state.clear()
    else:
        await state.clear()
        await start(message) 

@router.message(Admin_enter_to_panel.waiting_number)
async def process_admin_password(message: Message, state: FSMContext):
    if message.text == "8038":
        await message.answer("Привет, Админ!", reply_markup=kb.ADMIN_panel)
        await state.clear()
    else:
        await state.clear()
        await start(message)    

@router.message(F.text == "✏️ Добавить(уменьшить через (-)) деньги пользователю")
async def admin_change_money(message: Message, state: FSMContext):
    await message.answer("Введите id пользователя и нужное колличество денег, через пробел.")
    await state.set_state(Admin_change_money.waiting_number)

@router.message(Admin_change_money.waiting_number)
async def process_admin_change_money(message: Message, state: FSMContext):
    id, money = message.text.split()
    user.money_winner(id, money)
    await message.answer("Все готово!", reply_markup=kb.ADMIN_panel)
    await state.clear()

@router.message(F.text == "👥 Поиск профиля пользователя по id")
async def admin_finder_people(message: Message, state: FSMContext):
    await message.answer("Введите id пользователя")
    await state.set_state(Admin_finder_people.waiting_number)

@router.message(Admin_finder_people.waiting_number)
async def process_admin_finder_people(message: Message, state: FSMContext):
    stats = user.profile_stats(int(message.text))
    for i in stats:
        await message.answer(i, reply_markup=kb.ADMIN_panel)
    await state.clear()

@router.message(F.text == "💾 Сделать backup")
async def backup_database(message: Message):
    if message.from_user.id != YOUR_USER_ID:
        await message.answer("⛔ У вас нет прав для этой команды")
        return
    
    try:
        if not os.path.exists("infouser.db"):
            await message.answer("❌ Файл базы данных не найден")
            return
        
        with open("infouser.db", "rb") as f:
            db_data = f.read()
        
        await message.answer_document(
            BufferedInputFile(db_data, filename="infouser_backup.db"),
            caption="📦 Backup базы данных"
        )
        await message.answer("✅ База данных успешно экспортирована!")
        
    except Exception as e:
        await message.answer(f"❌ Ошибка при создании бэкапа: {e}")

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
    await message.answer(f"🆔 Ваш id - {message.from_user.id}")
    for i in stats:
        await message.answer(i, reply_markup=kb.main_menu)

@router.message(F.text == "🎰 Крутить слоты")
async def spin_slots(message: Message):
    await message.answer("Добро пожаловать в слоты! Каждая крутка будет стоить 50 вечно зеленых."
                         , reply_markup=kb.slots)

@router.message(F.text == "⬆️ Крутим")
async def spin_slots(message: Message):
    if user.minus_money(message.from_user.id) == "Деньги списаны.":
        user.how_much_u_lose(message.from_user.id, 50)
        user.slots_spin_add(message.from_user.id)
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
        elif result == casino_slots[-1] * 3:
            await message.answer("Поздравляю! Вы проебали 1000 вечно зеленых!")
            user.how_much_u_lose(message.from_user.id, 1000)
            user.money_winner(message.from_user.id, -1000)
    else:
        await message.answer("Бэйби ноу мани", reply_markup=kb.casino_menu)

@router.message(F.text == "🛞 Рулетка")
async def roulette(message: Message):
    await message.answer("Добро пожаловать в Европейскую рулетку! Каждая крутка обойдется в 50 вечно зеленых."
                         , reply_markup=kb.roulette)
    
@router.message(F.text == "🎯 Поставить на одно число")
async def roulette_one_num(message: Message, state: FSMContext):
    if user.minus_money(message.from_user.id) == "Деньги списаны.":
        user.how_much_u_lose(message.from_user.id, 50)
        user.roulette_spin_add(message.from_user.id)
        await message.answer("Хорошо, напишите пожалуйста число от 0 до 36 включительно",
                             reply_markup=ReplyKeyboardRemove())
        await state.set_state(RouletteStates_one.waiting_number)
    else:
        await message.answer("Бэйби ноу мани", reply_markup=kb.casino_menu)

@router.message(RouletteStates_one.waiting_number)
async def process_roulette_number(message: Message, state: FSMContext):
    user_number = message.text
    try:
        user_number = int(user_number)
        if 0 <= user_number <= 36:
            roulette_random_num = randint(0, 36)
            if user_number == roulette_random_num:
                user.how_much_u_won(message.from_user.id, 1750)
                user.money_winner(message.from_user.id, 1750)
                await message.answer("Поздравляю! Вы выиграли 1750 вечно зелененьких!", reply_markup=kb.roulette)
                await state.clear()
            else:
                await message.answer(f"Выпало число {roulette_random_num}. Вы проиграли.", reply_markup=kb.roulette)
            await state.clear()
        else:
            await message.answer("Число должно быть от 0 до 36 включительно", reply_markup=kb.roulette)
            await state.clear()
    except ValueError:
        await message.answer("Введите число от 0 до 36 включительно", reply_markup=kb.roulette)
        await state.clear()

@router.message(F.text == "🔴⚫🟢 Поставить на цвет")
async def roulette_one_num(message: Message, state: FSMContext):
    if user.minus_money(message.from_user.id) == "Деньги списаны.":
        user.how_much_u_lose(message.from_user.id, 50)
        user.roulette_spin_add(message.from_user.id)
        await message.answer("Хорошо, выберите цвет.", reply_markup=kb.roulette_color)
        await state.set_state(RouletteStates_two_color.waiting_number)
    else:
        await message.answer("Бэйби ноу мани", reply_markup=kb.casino_menu)

@router.message(RouletteStates_two_color.waiting_number)
async def process_roulette_color(message: Message, state: FSMContext):
    if message.text == "🔴":
        perc_color = 1
    elif message.text == "⚫":
        perc_color = 2
    elif message.text == "🟢":
        perc_color = 0
    else:
        await message.answer("Ну ты дурень конечно. Из двух ты выбрал хуй пойми что", reply_markup=kb.roulette)
        await state.clear()
        return
    dice_number = randint(0, 36)
    if dice_number == 0 and perc_color == 0:
        await message.answer("Поздравляю! Вы выиграли 1750 вечно зеленых", reply_markup=kb.roulette)
        await state.clear()
    elif dice_number % 2 == 0 and perc_color == 2:
        await message.answer("Поздравляю! Вы выиграли 80 вечно зеленых", reply_markup=kb.roulette)
        await state.clear()
    elif dice_number % 2 != 0 and perc_color == 1:
        await message.answer("Поздравляю! Вы выиграли 80 вечно зеленых", reply_markup=kb.roulette)
        await state.clear()
    else:
        if dice_number == 0:
            await message.answer("Вы проиграли! Цвет был: 🟢", reply_markup=kb.roulette)
            await state.clear()
        elif dice_number % 2 == 0:
            await message.answer("Вы проиграли! Цвет был: ⚫", reply_markup=kb.roulette)
            await state.clear()
        elif dice_number % 2 != 0:
            await message.answer("Вы проиграли! Цвет был: 🔴", reply_markup=kb.roulette)
            await state.clear()

@router.message(F.text == "🎲 Кости")
async def dice(message: Message):
    await message.answer("Добро пожаловать в dice! Каждый бросок будет стоить 50 вечно зеленых."
                         , reply_markup=kb.dice)

@router.message(F.text == "📦 Бросаем")
async def drop_dice(message: Message):
    if user.minus_money(message.from_user.id) == "Деньги списаны.":
        user.how_much_u_lose(message.from_user.id, 50)
        user.dice_drop_add(message.from_user.id)
        await message.answer("Деньги списаны!", reply_markup=kb.dice_game)
    else:
        await message.answer("Бэйби ноу мани", reply_markup=kb.casino_menu) 

@router.message(F.text == "🤔 Выбор одного числа")
async def dice_choose_one(message: Message, state: FSMContext):
    await message.answer("Выбери число", reply_markup=kb.dice_number_choose)
    await state.set_state(DiceStates_one.waiting_number)

@router.message(DiceStates_one.waiting_number)
async def choose_number(message: Message, state: FSMContext):
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
        await state.clear()
    dice_number = str(randint(1, 6))
    if perc_num == dice_number:
        user.how_much_u_won(message.from_user.id, 150)
        user.money_winner(message.from_user.id, 150)
        await message.answer("Поздравляю! Вы выиграли 150 вечно зеленых", reply_markup=kb.dice)
        await state.clear()
    else:
        await message.answer(f"Рандомным числом было - {dice_number}. Ты проиграл", reply_markup=kb.dice)
        await state.clear()

@router.message(F.text == "🤔 Выбор промежутка")
async def dice_choose_promezh(message: Message, state: FSMContext):
    await message.answer("Выбери промежуток чисел", reply_markup=kb.dice_number_choose_promezh)
    await state.set_state(DiceStates_many.waiting_number)
@router.message(DiceStates_many.waiting_number)
async def dice_chooses_pr(message: Message, state: FSMContext):
    if message.text == "1️⃣2️⃣":
        user_promezh = "12"
    elif message.text == "3️⃣4️⃣":
        user_promezh = "34"
    elif message.text == "5️⃣6️⃣":
        user_promezh = "56"
    else:
        await message.answer("Ну ты тупень. Выбирай из предложенных.", reply_markup=kb.dice)
        await state.clear()

    dice_number = str(randint(1, 6))
    if dice_number in user_promezh:
        user.how_much_u_won(message.from_user.id, 75)
        user.money_winner(message.from_user.id, 75)
        await message.answer("Поздравляю! Вы выиграли 75 вечно зеленых", reply_markup=kb.dice)
        await state.clear()
    else:
        await message.answer(f"Рандомным числом было - {dice_number}. Ты проиграл", reply_markup=kb.dice)
        await state.clear()