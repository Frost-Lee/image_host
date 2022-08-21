FROM python:3.9
WORKDIR /app
COPY . .
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install --upgrade setuptools pip
RUN pip3 install -r requirements.txt
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:1910", "app:app"]
