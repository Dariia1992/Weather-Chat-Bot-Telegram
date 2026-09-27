from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from states.weather import WeatherStates
from services.weather_api import get_weather
from keyboards.keyboard_main import kb_main


router = Router()


# Нажали inline-кнопку Change City
@router.callback_query(F.data == "change_city")
async def change_city(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(WeatherStates.choosing_city)

    await callback.message.answer("📍 Enter your city:")
    await callback.answer()


# Пользователь вводит город
@router.message(WeatherStates.choosing_city)
async def save_city(message: types.Message, state: FSMContext):
    city = message.text.strip()

    data = await get_weather(city)

    # Если город не найден
    if data.get("cod") != 200:
        await message.answer(
            "❌ City not found.\n"
            "Please enter another city:"
        )
        return

    # Сохраняем город
    await state.update_data(city=city)

    # Выходим из состояния выбора города
    await state.set_state(None)

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    description = data["weather"][0]["description"]

    await message.answer(
        f"🌤 Weather in {city}\n\n"
        f"🌡 Temperature: {temperature}°C\n"
        f"🤔 Feels like: {feels_like}°C\n"
        f"💧 Humidity: {humidity}%\n"
        f"💨 Wind: {wind} m/s\n"
        f"☁️ {description.capitalize()}",
        reply_markup=kb_main
    )