FROM python:3.8-slim
RUN pip install discord.py
RUN pip install python-dotenv
RUN pip install prometheus_client
RUN mkdir app
COPY bot.py /app
COPY prometheus.py /app
COPY start_discord /app
WORKDIR /app
RUN mkdir out
CMD [ "./start_discord" ]
