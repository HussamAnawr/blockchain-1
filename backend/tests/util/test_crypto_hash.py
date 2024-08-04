from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    assert crypto_hash(1, [2], "three") == crypto_hash([2], "three", 1)
    assert crypto_hash([2], "three", 1) == "6b1071734545aba8bcef4a545cfd4624f45771e7b14796a68a79b454adfefd75"