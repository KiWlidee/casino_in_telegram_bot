import sqlite3 as sq

with sq.connect("C:\\vscodepj\\casino_telegram_bot\\infouser.db") as db:   # C:\\vscodepj\\casino_telegram_bot\\ added
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS 
                   personality(telegram_id TEXT,
                   money INTEGER,
                   spins INTEGER,
                   dice_games INTEGER,
                   roulette_spins INTEGER,
                   money_lose INTEGER,
                   money_won INTEGER)""")


def add_znach_table():
    with sq.connect("C:\\vscodepj\\casino_telegram_bot\\infouser.db") as db:
        cursor = db.cursor()
        cursor.execute("""INSERT INTO personality VALUES('NULL', NULL,NULL,NULL,NULL,NULL,NULL)""")
    

def user_find(name):
    with sq.connect("C:\\vscodepj\\casino_telegram_bot\\infouser.db") as db:
        cursor = db.cursor()
        cursor.execute(f"""SELECT telegram_id FROM personality WHERE telegram_id == '{name}'""")
        if cursor.fetchall() == [] or cursor.fetchall() == 'NULL':
            return True
        else:
            return False
        

def start_username_add(name):
    if user_find(name):
        with sq.connect("C:\\vscodepj\\casino_telegram_bot\\infouser.db") as db:
            cursor = db.cursor()
            cursor.execute(f"""UPDATE personality SET telegram_id = '{name}' WHERE telegram_id == 'NULL'""")


def profile_stats(id):
    with sq.connect("C:\\vscodepj\\casino_telegram_bot\\infouser.db") as db:
        cursor = db.cursor()
        cursor.execute(f"""SELECT money, spins, dice_games, roulette_spins, money_lose, money_won 
                       FROM personality WHERE telegram_id == '{id}'""")
        x = cursor.fetchall()
        balance = f"💵 Баланс - {x[0][0]}"
        spins = f"🎰 Колличество круток - {x[0][1]}"
        dice_games = f"🎲 Колличесво игр в кости - {x[0][2]}"
        roulette_spins = f"🛞 Колличесво круток в рулетке - {x[0][3]}"
        money_lose = f"💸 Сколько ты проиграл - {x[0][4]}"
        money_won = f"💸 Сколько ты выиграл - {x[0][5]}"
        return balance, spins, dice_games, roulette_spins, money_lose, money_won


def start_profile_stats(id):
    with sq.connect("C:\\vscodepj\\casino_telegram_bot\\infouser.db") as db:
        cursor = db.cursor()
        cursor.execute(f"""UPDATE personality SET money = 10000 WHERE telegram_id == '{id}'""")
        cursor.execute(f"""UPDATE personality SET spins = 0 WHERE telegram_id == '{id}'""")
        cursor.execute(f"""UPDATE personality SET dice_games = 0 WHERE telegram_id == '{id}'""")
        cursor.execute(f"""UPDATE personality SET roulette_spins = 0 WHERE telegram_id == '{id}'""")
        cursor.execute(f"""UPDATE personality SET money_lose = 0 WHERE telegram_id == '{id}'""")
        cursor.execute(f"""UPDATE personality SET money_won = 0 WHERE telegram_id == '{id}'""")
    

def how_much_u_lose(id, money):
    with sq.connect("C:\\vscodepj\\casino_telegram_bot\\infouser.db") as db:
        cursor = db.cursor()
        cursor.execute(f"""UPDATE personality SET money_lose = money_lose + {money} WHERE telegram_id == '{id}'""")


def how_much_u_won(id, money):
    with sq.connect("C:\\vscodepj\\casino_telegram_bot\\infouser.db") as db:
        cursor = db.cursor()
        cursor.execute(f"""UPDATE personality SET money_won = money_won + {money} WHERE telegram_id == '{id}'""")


def slots_spin_add(id):
    with sq.connect("C:\\vscodepj\\casino_telegram_bot\\infouser.db") as db:
        cursor = db.cursor()
        cursor.execute(f"""UPDATE personality SET spins = spins + 1 WHERE telegram_id == '{id}'""")


def minus_money(id):
    with sq.connect("C:\\vscodepj\\casino_telegram_bot\\infouser.db") as db:
        cursor = db.cursor()
        cursor.execute(f"""UPDATE personality SET money = money - 50 WHERE telegram_id == '{id}' AND money >= 50""")
        if cursor.rowcount > 0:
            return "Деньги списаны."
        else:
            return "Недостаточно средств."
        
def money_winner(id, money):
    with sq.connect("C:\\vscodepj\\casino_telegram_bot\\infouser.db") as db:
        cursor = db.cursor()
        cursor.execute(f"""UPDATE personality SET money = money + {money} WHERE telegram_id == '{id}'""")


def dice_drop_add(id):
    with sq.connect("C:\\vscodepj\\casino_telegram_bot\\infouser.db") as db:
        cursor = db.cursor()
        cursor.execute(f"""UPDATE personality SET dice_games = dice_games + 1 WHERE telegram_id == '{id}'""")


def roulette_spin_add(id):
    with sq.connect("C:\\vscodepj\\casino_telegram_bot\\infouser.db") as db:
        cursor = db.cursor()
        cursor.execute(f"""UPDATE personality SET roulette_spins = roulette_spins + 1 WHERE telegram_id == '{id}'""")

