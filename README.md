# TORUS

Ticker: TRS \
Proof of Stake: 5% yearly rate \
Min. stake age: 8 hours \
Block time: 120 sec

Burn address: [TEuWjbJPZiuzbhuS6YFE5v4gGzkkt26HDJ](https://explorer.torus.cc/address/TEuWjbJPZiuzbhuS6YFE5v4gGzkkt26HDJ) \
[See](contrib/burn-address.py) for more details.

*****************************

## Run a node

Torus full node can be run using a prebuild Docker image. This is recommended as the image is under the active development. \
Image tagged as `latest` will always match the master branch.
If you want to run a stable release, use the image tag that corresponds to the official release - e.g. `torusd:1.0.0`.

Pull image:
```bash
docker pull ghcr.io/torus-economy/torusd:latest
```

Run container:
```bash
docker run \
    -d \
    -p 24111:24111 \
    -v /home/$USER/.TORUS:/root/.TORUS \
    --name TORUSd \
    --restart=always \
    ghcr.io/torus-economy/torusd:latest
```

or with RPC port enabled:
```bash
docker run \
    -d \
    -p 24111:24111 \
    -p 24112:24112 \
    -v /home/$USER/.TORUS:/root/.TORUS \
    --name TORUSd \
    --restart=always \
    ghcr.io/torus-economy/torusd:latest
```

Make sure to have a valid `TORUS.conf` file in `/home/$USER/.TORUS/TORUS.conf` or in any other path that was specified.
For more information about configuration file see [example](TORUS.conf).
Docker container must always have torusd process running in the foreground, so do not include `daemon=1` in `TORUS.conf` configuration file when running within Docker.
In case `daemon=1` is included, the Docker process will exit immediately.

Minimum `TORUS.conf` configuration file should include the following:

```bash
rpcuser=rpc
rpcpassword=password123
server=1
listen=1
```

#### docker-compose

This could also be achived by running a docker-compose script.
Preconfigured docker-compose script with corresponding `TORUS.conf` configuration file can be found in [contrib](contrib/docker-compose) folder.
For security reasons, make sure to change `rpcuser` and `rpcpassword` default values.
Afterwards, the script can be run:

```bash
cd contrib/docker-compose
docker-compose up -d
```

#### Seed nodes

Official seed nodes:

- 185.150.117.203
- 185.150.117.219
- 84.32.188.71

Official DNS seed servers:

- dnsseed1.torus.cc
- dnsseed2.torus.cc
- dnsseed3.torus.cc

### Build from source

In order to build from source, check out [docs](doc).

## Release notes

To see release notes check out this [file](doc/release-notes.md).
