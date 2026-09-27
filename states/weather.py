from aiogram.fsm.state import State, StatesGroup


class WeatherStates(StatesGroup):
    choosing_city = State()