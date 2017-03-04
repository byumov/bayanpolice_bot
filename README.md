bayanpolice_bot is a simple bot for Telergam.
Bot parse all messages in chat and send funny images.
### Requirements
```
sudo apt update; sudo apt install -y python3 python3-pip; sudo pip3 install pyTelegramBotAPI
```
Get API key from @BotFather - https://core.telegram.org/bots#botfather
### Run
From command line: `python3 run_bot.py "YOUR_API_KEY"`

Docker:
```
cd bayanpolice_bot
sudo docker build -t bayanpolice_bot .
sudo docker run --env API_KEY="YOUR_API_KEY" -d --name bayan_bot bayanpolice_bot
```
