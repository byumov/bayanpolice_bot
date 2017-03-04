FROM python:3.5

COPY files /opt/bot
RUN pip install pyTelegramBotAPI

ENTRYPOINT  python /opt/bot/run_bot.py $API_KEY
