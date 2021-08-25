FROM ubuntu:16.04 as torus-core

LABEL maintainer="Sven Skender (@sskender)"

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

RUN apt-get install \
    libboost-all-dev \
    libminiupnpc-dev \
    libqrencode-dev \
    libssl-dev \
    libzmq-dev \
    -y

# BerkeleyDB v4.8.30.NC
WORKDIR /opt

ENV BERKELEYDB_VERSION=db-4.8.30.NC
RUN wget "http://download.oracle.com/berkeley-db/${BERKELEYDB_VERSION}.tar.gz"
RUN tar -xvzf ${BERKELEYDB_VERSION}.tar.gz

WORKDIR /opt/${BERKELEYDB_VERSION}/build_unix
RUN ../dist/configure --with-static --enable-cxx --disable-shared --with-pic --prefix=/usr/local && \
    make -j$(nproc) && \
    make install

WORKDIR /opt
RUN rm ${BERKELEYDB_VERSION}.tar.gz
RUN rm -r ${BERKELEYDB_VERSION}

# headless daemon
WORKDIR /opt/torus-core
COPY . .

RUN cd src/ && \
    make -f makefile.unix -j$(nproc) && \
    strip TORUSd

WORKDIR /opt
RUN mv torus-core/src/TORUSd TORUSd
RUN rm -r torus-core

EXPOSE 12411 22411 32411 42411

VOLUME ["/root/.TORUS"]

CMD ["./TORUSd"]
