FROM python:3.9
WORKDIR /app
COPY . .
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install --upgrade setuptools pip
RUN pip3 install -r requirements.txt

# Create a shell script to handle environment variable expansion
RUN echo '#!/bin/sh\nexec gunicorn --workers 4 --bind 0.0.0.0:${IMAGE_HOST_PORT} app:app' > /app/start.sh && \
    chmod +x /app/start.sh

CMD ["/app/start.sh"]
