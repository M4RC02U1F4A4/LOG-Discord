FROM python:3.8-slim
RUN pip install discord.py
RUN pip install python-dotenv
RUN mkdir app
COPY . /app
WORKDIR /app
RUN mkdir out
CMD [ "python", "./bot.py" ]
