FROM python:3.8
RUN mkdir -p /app
WORKDIR /app
RUN pip install uvicorn
COPY requirements.txt .
RUN pip3 install -r /app/requirements.txt

EXPOSE 8000

COPY . .


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]