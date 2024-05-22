FROM python:3.12-alpine3.18

# Set the working directory
WORKDIR /app

# Setup dependancies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy the app code
COPY . /app

# Run the app
CMD ["python", "app.py"]
