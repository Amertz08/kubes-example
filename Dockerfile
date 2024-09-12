FROM python:3.12-slim

EXPOSE 8000

RUN mkdir /opt/kube-app
WORKDIR /opt/kube-app

COPY requirements.txt .

RUN python3.12 -m pip install --upgrade \
    pip \
    setuptools \
    wheel

RUN python3.12 -m pip install --no-cache-dir -r requirements.txt

COPY src/ .

CMD ["fastapi", "run", "main.py"]
