import base58
import hashlib


#
# Burn address: TEuWjbJPZiuzbhuS6YFE5v4gGzkkt26HDJ
#


def generate_ecdsa_publickey():
    # ECDSA public key without existing private key
    ecdsa_publickey = '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    print("ecdsa_public_key = \t" + ecdsa_publickey)
    assert(len(ecdsa_publickey) / 2 == 65)  # 65 bytes
    return ecdsa_publickey


def compress_pubkey(ecdsa_publickey):
    # https://en.bitcoin.it/wiki/Protocol_documentation#Signatures
    if ord(bytearray.fromhex(ecdsa_publickey[-2:])) % 2 == 0:
        prefix = "02"
    else:
        prefix = "03"
    ecdsa_publickey_compressed = prefix + ecdsa_publickey[2:66]
    print("compressed_ecdsa_public_key = \t" + ecdsa_publickey_compressed)
    assert(len(ecdsa_publickey_compressed) / 2 == 33)  # 33 bytes
    return ecdsa_publickey_compressed


def hash160(ecdsa_publickey):
    # https://en.bitcoin.it/wiki/Protocol_documentation#Addresses
    ecdsa_publickey_hex = bytearray.fromhex(ecdsa_publickey)
    sha = hashlib.sha256()
    rip = hashlib.new('ripemd160')
    sha.update(ecdsa_publickey_hex)
    print("sha256_hash = \t" + sha.hexdigest())
    rip.update(sha.digest())
    print("ripemd160_hash = \t" + rip.hexdigest())
    rip160_hash = rip.hexdigest()
    assert(len(rip160_hash) / 2 == 20)  # 160 bits = 20 bytes
    return rip160_hash


def create_pub_key_hash(ecdsa_publickey_hash):
    prefix = "41"  # letter "T"
    pub_key_hash = prefix + ecdsa_publickey_hash
    print("pub_key_hash = \t" + pub_key_hash)
    assert(len(pub_key_hash) / 2 == 21)  # 21 bytes
    return pub_key_hash


def calculate_checksum(pub_key_hash):
    # https://en.bitcoin.it/wiki/Protocol_documentation#Addresses
    pub_key_hash_hex = bytearray.fromhex(pub_key_hash)
    sha1 = hashlib.sha256()
    sha2 = hashlib.sha256()
    sha1.update(pub_key_hash_hex)
    print("sha256_hash_1 = \t" + sha1.hexdigest())
    sha2.update(sha1.digest())
    print("sha256_hash_2 = \t" + sha2.hexdigest())
    sha256_sha256_hash = sha2.hexdigest()
    # checksum is the first 4 bytes
    checksum = sha256_sha256_hash[:8]
    print("checksum = \t" + checksum)
    assert(len(checksum) / 2 == 4)  # 4 bytes
    return checksum


def base58_convert(pub_key_hash, checksum):
    full_hash = pub_key_hash + checksum
    print("full_hash = \t" + full_hash)
    assert(len(full_hash) / 2 == 25)  # 25 bytes
    full_hash_hex = bytearray.fromhex(full_hash)
    encoded_address = base58.b58encode(full_hash_hex)
    decoded_address = encoded_address.decode("utf-8")
    print("decoded_address = \t" + decoded_address)
    assert(len(decoded_address) == 34)  # 34 characters
    return decoded_address


def main():
    # generate new ecdsa public key
    ecdsa_publickey = generate_ecdsa_publickey()

    # compress ecdsa public key
    compress = True
    if compress:
        ecdsa_publickey = compress_pubkey(ecdsa_publickey)

    # hash ecdsa public key
    ecdsa_publickey_hash = hash160(ecdsa_publickey)

    # create public key hash from ecdsa public key hash and add prefix
    pub_key_hash = create_pub_key_hash(ecdsa_publickey_hash)

    # calculate checksum from public key hash
    checksum = calculate_checksum(pub_key_hash)

    # create address from public key hash and checksum
    torus_burn_address = base58_convert(pub_key_hash, checksum)
    print("Torus burn address = \t" + torus_burn_address)


if __name__ == "__main__":
    main()
