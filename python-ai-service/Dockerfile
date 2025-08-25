FROM python:3.12-slim

WORKDIR /app

# Copy requirements file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

EXPOSE 5000

# Run the app with uvicorn
CMD ["uvicorn", "fast:app", "--host", "0.0.0.0", "--port", "5000"]
