
# 1. Start with a lightweight version of Python (Linux based)
FROM python:3.13-slim-trixie

# 2. Create a folder inside the container to hold your app
WORKDIR /matrix-pinger

# 3. Copy your requirements file into the container
COPY requirements.txt .

# 4. Install the dependencies inside the container
RUN apt-get update                  && \
    apt-get install g++ make -y     && \
    pip install -r requirements.txt && \
    apt-get purge g++ make -y       && \
    apt-get autoremove -y

# 5. Copy the rest of your bot code into the container
COPY . .

# 6. The command to run your bot when the container starts
CMD ["python3", "main.py"]
