
FROM python:3.9.16-slim AS final
# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP /usr/src/app/src/app.py

# Install app dependencies
COPY ./requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /usr/src/app

# Run the application
CMD python3 -m flask run