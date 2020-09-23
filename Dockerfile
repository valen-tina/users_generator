FROM python
WORKDIR /code
COPY *.json ./
COPY *.py ./

CMD python randomAdvocatesGenerator.py