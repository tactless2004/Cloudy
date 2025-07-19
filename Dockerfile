FROM python:3.12-slim

WORKDIR /src

COPY . /src

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "UI.py"]