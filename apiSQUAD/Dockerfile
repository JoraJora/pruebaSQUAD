FROM python:latest
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/

EXPOSE 5004
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

RUN rm -rf flask-apispec
RUN git clone https://github.com/jmcarp/flask-apispec.git
RUN CMD [ "python3", "flask-apispec/setup.py" ]

CMD ["python", "app.py"]
