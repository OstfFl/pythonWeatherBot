# pythonWeatherBot
Python Weather Bot
Description:
  A simple weather bot written in Python using the telebot library and the OpenWeatherMap API. The bot allows users to obtain weather information for different cities based on the provided data from the OpenWeatherMap API. Additionally, the bot offers interactive and humorous responses depending on the current weather conditions.

Features
Welcome:

The bot greets the user upon starting with the /start command and sends an animated sticker to give the interaction a friendly character.
Help:
  The /help command displays basic bot commands, making it easy for the user to understand the bot's functions and use them effectively.

Weather:
  The bot responds to a text message containing the name of a city, providing weather information from the OpenWeatherMap API.
  Depending on the temperature, the bot sends an animated sticker and an additional description, giving the interaction a humorous tone.
Commands:
  /start - Launches the bot and displays a welcome message with an animated sticker.
  /help - Displays basic bot commands, helping the user navigate and utilize the bot's features.
  
Technologies Used:
  Programming Language: Python
  Telegram Bot API Library: telebot
  Other: PytelegramBotApi, pyowm
  Weather API: OpenWeatherMap
Configuration:
  Paste your OpenWeatherMap API key into the api_weather variable.
  Paste your Telegram API key from BotFather into the api_telegram variable.
Notes:
  Internet connectivity is required, along with properly configured OpenWeatherMap and Telegram API keys.
Customization:
  The bot can be customized to fit personal preferences by adding new commands, changing reactions to weather conditions, and personalizing welcome messages.
Author:
  OstfFl (GitHub: OstfFl)
