# Base image is the python 3.7 docker image
FROM python:3.7

# Set the working directory inside the image
WORKDIR /home/crnlpanic/public_html

# Copy from the build context to the image
COPY . .

# Install requirements
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Set the entrypoint
ENTRYPOINT python3.7 app.py
