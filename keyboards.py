from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

register = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="✍ Зарегистрироваться / 🔑 Войти")
]], resize_keyboard=True)


casino_menu = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="➡️ Перейти в основное меню")
]], resize_keyboard=True)


main_menu = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="🪪 Профиль"),
    KeyboardButton(text="🎰 Крутить слоты"),
    KeyboardButton(text="🛞 Рулетка"),
    KeyboardButton(text="🎲 Кости"),
    KeyboardButton(text="🔚 Выйти")
]], resize_keyboard=True)

slots = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="⬆️ Крутим"),
    KeyboardButton(text="➡️ Перейти в основное меню")
]], resize_keyboard=True)

dice = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="📦 Бросаем"),
    KeyboardButton(text="➡️ Перейти в основное меню")
]], resize_keyboard=True)

dice_game = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="🤔 Выбор одного числа"),
    KeyboardButton(text="🤔 Выбор промежутка")
]], resize_keyboard=True)

dice_number_choose = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="1️⃣"),
    KeyboardButton(text="2️⃣"),
    KeyboardButton(text="3️⃣"),
    KeyboardButton(text="4️⃣"),
    KeyboardButton(text="5️⃣"),
    KeyboardButton(text="6️⃣"),
]], resize_keyboard=True)

dice_number_choose_promezh = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="1️⃣2️⃣"),
    KeyboardButton(text="3️⃣4️⃣"),
    KeyboardButton(text="5️⃣6️⃣"),
]], resize_keyboard=True)


roulette = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="🎯 Поставить на одно число"),
    KeyboardButton(text="🔴⚫🟢 Поставить на цвет"),
    KeyboardButton(text="➡️ Перейти в основное меню")
]], resize_keyboard=True)

roulette_color = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="🔴"),
    KeyboardButton(text="⚫"),
    KeyboardButton(text="🟢")
]], resize_keyboard=True)