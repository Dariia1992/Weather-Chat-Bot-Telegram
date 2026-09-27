from aiogram import types


button_forecast = types.InlineKeyboardButton(
    text="📅 5-Day Forecast",
    callback_data="forecast"
)

button_change_city = types.InlineKeyboardButton(
    text="📍 Change City",
    callback_data="change_city"
)

button_exit = types.InlineKeyboardButton(
    text="🚪 Exit",
    callback_data="exit"
)


keyboard_main = [
    [button_forecast],
    [button_change_city, button_exit]
]


kb_main = types.InlineKeyboardMarkup(
    inline_keyboard=keyboard_main
)