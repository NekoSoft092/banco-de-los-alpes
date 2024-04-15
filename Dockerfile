# Use the official Python image as the base

FROM python:3.11 

# Set the working directory inside the container
WORKDIR /app

# Copy your FastAPI app code into the container
COPY . /app

# Install FastAPI and Uvicorn
RUN pip install -e ".[all]"

# Expose port 8080
EXPOSE 8080

# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

