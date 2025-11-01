# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy project files (excluding those in .dockerignore / .gitignore)
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --timeout=300 --retries=5 -r requirements.txt

# Run the chatbot
CMD ["python", "chatbot.py"]

