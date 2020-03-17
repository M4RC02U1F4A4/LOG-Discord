FROM python:3.8
RUN pip install discord.py
RUN pip install python-dotenv
RUN mkdir app
COPY . /app
WORKDIR /app
CMD [ "python", "./bot.py" ]
