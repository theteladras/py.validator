from typing import Literal, Union

from .utils.assert_string import assert_string

HashAlgorithms = Union [
    Literal["md5"],
    Literal["md4"],
    Literal["sha1"],
    Literal["sha256"],
    Literal["sha384"],
    Literal["sha512"],
    Literal["ripemd128"],
    Literal["ripemd160"],
    Literal["tiger128"],
    Literal["tiger160"],
    Literal["tiger192"],
    Literal["crc32"],
    Literal["crc32b"]
]

hash_lengths = {
  "md5": 32,
  "md4": 32,
  "sha1": 40,
  "sha256": 64,
  "sha384": 96,
  "sha512": 128,
  "ripemd128": 32,
  "ripemd160": 40,
  "tiger128": 32,
  "tiger160": 40,
  "tiger192": 48,
  "crc32": 8,
  "crc32b": 8,
}

def is_hash(input: str, algorithm: HashAlgorithms) -> bool:
    input = assert_string(input)
    pattern = "^[a-fA-F0-9]{" + str(hash_lengths[algorithm]) + "}$"
    return input.match(pattern)
