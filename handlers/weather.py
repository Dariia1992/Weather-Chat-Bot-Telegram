from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from services.weather_api import get_forecast
from keyboards.keyboard_main import kb_main


router = Router()


@router.callback_query(F.data == "forecast")
async def forecast(callback: types.CallbackQuery, state: FSMContext):
    data_state = await state.get_data()
    city = data_state.get("city")

    if not city:
        await callback.message.answer("📍 Please enter your city first.")
        await callback.answer()
        return

    data = await get_forecast(city)

    if str(data.get("cod")) != "200":
        await callback.message.answer(
            "❌ Forecast is unavailable. Please try again."
        )
        await callback.answer()
        return

    forecast_list = data["list"]

    text = f"📅 5-Day Forecast for {city}\n\n"

    for item in forecast_list:
        if "12:00:00" in item["dt_txt"]:
            date = item["dt_txt"].split(" ")[0]
            temperature = item["main"]["temp"]
            description = item["weather"][0]["description"]

            text += (
                f"📆 {date}\n"
                f"🌡 Temperature: {temperature}°C\n"
                f"☁️ {description.capitalize()}\n\n"
            )

    await callback.message.answer(
        text,
        reply_markup=kb_main
    )

    await callback.answer()