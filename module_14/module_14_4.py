from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import crud_functions
import asyncio

crud_functions.initiate_db()

api = ""

bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard = True)
button1 = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
button5 = KeyboardButton(text="Купить")
kb.add(button1)
kb.add(button2)
kb.add(button5)

kb_in = InlineKeyboardMarkup(resize_keyboard = True)
button3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_in.add(button3)
kb_in.add(button4)

kb_sell = InlineKeyboardMarkup(resize_keyboard = True)
button6 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button7 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button8 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button9 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb_sell.add(button6)
kb_sell.add(button7)
kb_sell.add(button8)
kb_sell.add(button9)

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb)
    await message.answer('Хотите рассчитать свою норму калорий в день?')


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    products = crud_functions.get_all_products()
    for  id, title, description, price in products:
        await message.answer(f'Название: {title} | Описание: {description} | Цена: {price}')
        with open(f'{id}.jpeg', "rb") as img:
            await message.answer_photo(img)
    await message.answer("Выберите продукт для покупки:", reply_markup=kb_sell)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_in)


@dp.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("Формула для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()


@dp.message_handler(text="Информация")
async def information(message):
    await message.answer('Пока нет информации')


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    await message.answer(f'Средняя норма калорий в день:'
                         f' {10 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5 * float(data["age"]) - 161}')
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)