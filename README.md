# TORUS

Ticker: TRS \
Proof of Stake: 5% yearly rate \
Min. stake age: 8 hours \
Block time: 120 sec

*****************************

## Run a node

Torus full node can be run using a prebuild Docker image. \
Image tagged as `latest` will always match the master branch.
If you want to run a stable release, use the image tag that corresponds to the official release - e.g. `torusd:1.0.0`.

Pull image:
```bash
docker pull ghcr.io/torus-economy/torusd:latest
```

Run container:
```bash
docker run -d -p 24111:24111 -v /home/$USER/.TORUS:/root/.TORUS ghcr.io/torus-economy/torusd:latest
```

or with RPC port enabled:
```bash
docker run -d -p 24111:24111 -p 24112:24112 -v /home/$USER/.TORUS:/root/.TORUS ghcr.io/torus-economy/torusd:latest
```

Make sure to have a valid `.TORUS.conf` file in `/home/$USER/.TORUS/TORUS.conf`. For more info see [example](TORUS.conf).

### Build from source

In order to build from source, check out [docs](doc).
