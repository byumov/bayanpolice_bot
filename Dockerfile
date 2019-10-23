FROM python:3.5

COPY . /opt/bot
RUN pip install -r requirements.txt

ENTRYPOINT  python /opt/bot/run_bot.py $API_KEY
