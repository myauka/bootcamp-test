import hashlib


def hash_string(some_string: str):
    hash_object = hashlib.sha1(str.encode(some_string))
    hex_dig = hash_object.hexdigest()
    print(hex_dig)


YOUR_STRING = ''  # put your string here
hash_string(YOUR_STRING)
