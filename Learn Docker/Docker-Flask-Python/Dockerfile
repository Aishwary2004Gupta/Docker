FROM python:3-alpine3.19

WORKDIR /myApp

COPY . /myApp

RUN pip install -r requirements.txt

EXPOSE 3030

CMD python ./index.py