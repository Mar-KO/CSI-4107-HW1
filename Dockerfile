FROM python:3

WORKDIR /homework1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python3 -m spacy download en_core_web_sm

COPY . .

CMD [ "python", "./homework1.py" ]