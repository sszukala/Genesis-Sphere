FROM ubuntu:20.04

# Set noninteractive mode for apt
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages and development tools
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    python3 \
    python3-pip \
    python3-dev \
    cmake \
    vim \
    nano \
    wget \
    curl \
    gfortran \
    libhdf5-dev \
    libopenmpi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages for analysis
RUN pip3 install numpy matplotlib h5py scipy astropy

# Set up a helper script for rebuilding
RUN echo '#!/bin/bash\ncd /athena\npython3 configure.py --prob=blast --coord=spherical_polar --flux=hllc\nmake clean\nmake -j$(nproc)' > /usr/local/bin/rebuild-athena \
    && chmod +x /usr/local/bin/rebuild-athena

# Clone Athena repository
RUN git clone https://github.com/PrincetonUniversity/athena.git /athena

# Build Athena
WORKDIR /athena
RUN python3 configure.py --prob=blast --coord=spherical_polar --flux=hllc
RUN make -j$(nproc)

# Create scripts to run example problems
RUN echo '#!/bin/bash\ncd /athena\n./bin/athena -i inputs/hydro/athinput.blast' > /usr/local/bin/run-blast \
    && chmod +x /usr/local/bin/run-blast

# Create a directory for analysis scripts
RUN mkdir -p /analysis
COPY athena_analysis.py /analysis/

# Set environment variables
ENV PATH="/athena/bin:${PATH}"

# Set working directory to shared volume
WORKDIR /workspace

# Welcome message
RUN echo 'echo "Welcome to Athena MHD Docker environment!"' >> /root/.bashrc
RUN echo 'echo "- To rebuild Athena: run rebuild-athena"' >> /root/.bashrc
RUN echo 'echo "- To run the blast problem: run-blast"' >> /root/.bashrc
RUN echo 'echo "- Analysis scripts are in /analysis"' >> /root/.bashrc

CMD ["/bin/bash"]