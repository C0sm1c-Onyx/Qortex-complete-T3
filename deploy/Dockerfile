FROM python3.8

LABEL authors="Astral Onyx"

WORKDIR usr/src/app

COPY requirements.txt ./

RUN pip install -r ./requirements.txt

COPY . .