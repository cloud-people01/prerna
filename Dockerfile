FROM python:3.10-alpine
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
# RUN apt update && apt install -y vim
COPY src /app
CMD python /app/app.py