from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states.weather import WeatherStates


router = Router()


@router.message(Command("start"))
async def command_start(message: types.Message, state: FSMContext):
    await state.set_state(WeatherStates.choosing_city)

    await message.answer(
        "🌤 Welcome to Weather Bot!\n\n"
        "Here you can check the current weather "
        "and 5-day forecast for your city.\n\n"
        "📍 Please enter your city:"
    )


@router.message(Command("stop"))
async def command_stop(message: types.Message, state: FSMContext):
    await state.clear()

    await message.answer("Goodbye 👋")


@router.callback_query(F.data == "exit")
async def exit_bot(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()

    await callback.message.edit_reply_markup(
        reply_markup=None
    )

    await callback.message.answer("Goodbye 👋")

    await callback.answer()