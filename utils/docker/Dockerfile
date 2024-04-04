FROM python:3.8

RUN pip install selenium

RUN apt-get update && apt-get install -y firefox-esr

WORKDIR /app

CMD ["tail", "-f", "/dev/null"]
