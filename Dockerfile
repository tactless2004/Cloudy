FROM python:3.12-slim

WORKDIR /src

COPY . /src

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /src/TUI

CMD ["python3", "cloudy_textual_ui.py"]