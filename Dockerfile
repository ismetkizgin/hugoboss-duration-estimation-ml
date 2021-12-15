FROM python:3.9

WORKDIR /usr/src/app

COPY . ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python ./model.py

CMD [ "python", "./app.py" ]