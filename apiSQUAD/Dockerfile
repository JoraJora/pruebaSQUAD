FROM python:latest
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/

EXPOSE 5004
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python", "app.py"]
