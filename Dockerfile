FROM ubuntu:16.04 as build

RUN apt-get update -y

RUN apt-get install \
    apt-utils \
    pkg-config \
    -y

RUN apt-get install \
    automake \
    bsdmainutils \
    cmake \
    curl \
    libtool \
    make \
    python3 \
    wget \
    -y

# Dependencies
RUN apt-get install \
    libboost-all-dev \
    libminiupnpc-dev \
    libqrencode-dev \
    libssl-dev \
    -y

# BerkeleyDB v4.8
# WORKDIR /
# RUN wget "http://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz"
# RUN tar -xvzf db-4.8.30.NC.tar.gz
# WORKDIR /db-4.8.30.NC/build_unix
# RUN ../dist/configure --with-static --enable-cxx --prefix=/usr/local && \
#     make && \
#     make install

# BerkeleyDB v5.3
RUN apt-get install \
    libdb-dev \
    libdb++-dev \
    -y

# Build daemon
WORKDIR /shrooms
COPY . .
RUN cd src/ && \
    make -f makefile.unix

