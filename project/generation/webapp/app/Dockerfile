
FROM python:3.9.16-slim AS final
# Set work directory
WORKDIR /usr/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP /usr/app/src/app.py

# Install app dependencies
COPY ./requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /usr/app

# Run the application
CMD python3 -m flask run --debug --host=0.0.0.0
