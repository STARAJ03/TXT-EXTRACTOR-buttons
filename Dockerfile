FROM python:latest

# Install system dependencies needed for building packages
RUN apt update && apt upgrade -y && \
    apt install -y git curl python3-pip ffmpeg aria2 build-essential python3-dev liblz4-dev libssl-dev libffi-dev cmake pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, and wheel
RUN pip3 install --upgrade pip setuptools wheel

# Copy requirements file
COPY requirements.txt /requirements.txt

# Install python dependencies
RUN pip3 install -U -r /requirements.txt

# Create working directory and set it
RUN mkdir /EXTRACTOR
WORKDIR /EXTRACTOR

# Copy start script
COPY start.sh /start.sh

# Fix permissions (optional but recommended)
RUN chmod +x /start.sh

# Run your start script
CMD ["/bin/bash", "/start.sh"]
