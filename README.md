# 🌤 Weather Telegram Bot

A Telegram weather bot built with Python and aiogram.

The bot allows users to enter a city, check the current weather, and view a 5-day weather forecast.

## ✨ Features

- 📍 Search weather by city
- 🌡 Current temperature
- 🤔 Feels-like temperature
- 💧 Humidity
- 💨 Wind speed
- ☁️ Weather description
- 📅 5-day weather forecast
- 🔄 Change city
- 🚪 Exit from the bot
- ❌ City validation and error handling
- 🔘 Inline keyboard navigation

## 🛠 Technologies

- Python
- aiogram 3
- aiohttp
- OpenWeather API
- python-dotenv
- Telegram Bot API
- FSM (Finite State Machine)

## 📁 Project Structure

weather_bot/
├── handlers/
│   ├── commands.py
│   ├── city.py
│   ├── weather.py
│   └── echo.py
├── keyboards/
│   └── keyboard_main.py
├── services/
│   └── weather_api.py
├── states/
│   └── weather.py
├── config.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

## 🚀 How It Works

1. Start the bot with `/start`
2. Enter your city
3. The bot displays the current weather
4. Use the inline keyboard to:
   - view the 5-day forecast
   - change the city
   - exit the bot

## 🔐 Environment Variables

Create a `.env` file:

TOKEN_TG=your_telegram_bot_token
TOKEN_OWM=your_openweather_api_key

The `.env` file is excluded from Git using `.gitignore`.

## 📦 Installation

Install dependencies:

pip install -r requirements.txt

Run the bot:

python main.py

## 👩‍💻 Author

Dariia Vasileva

Python Backend Developer in training