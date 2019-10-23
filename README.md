# Bayan police bot

@Bayanpolice_bot is a simple bot for Telergam.

The bot parse all messages in group and send funny images.
### Requirements

* python > 3
* pyTelegramBotAPI
* API key from @BotFather - https://core.telegram.org/bots#botfather

### Quick start

Linux: 
```
git clone https://github.com/byumov/bayanpolice_bot/
cd bayanpolice_bot
python3 run_bot.py "YOUR_API_KEY"
```

Docker:
```
sudo docker run --env API_KEY="YOUR_API_KEY" -d --name bayan_bot byumov/bayanpolice_bot
```
