# Use an official Ubuntu base image
FROM ubuntu:20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8

# Install necessary system packages
RUN apt-get update && apt-get install -y \
    wget \
    bzip2 \
    ca-certificates \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh && \
    $CONDA_DIR/bin/conda clean -tipsy

# Update PATH environment variable
ENV PATH=$CONDA_DIR/bin:$PATH

# Create and activate a Conda environment
COPY environment.yml .
RUN conda env create -f environment.yml && conda clean -a

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "rag-env", "/bin/bash", "-c"]

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Specify the default command
CMD ["conda", "run", "-n", "rag-env", "python", "main.py"]
