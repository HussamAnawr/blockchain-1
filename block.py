from time import time_ns
from crypto_hash import crypto_hash

GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
}

class Block:

    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp =  timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self) -> str:
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data})\n'
        )
    
    @staticmethod
    def mine_block(last_block, data):
        timestamp = time_ns()
        last_hash = last_block.hash
        hash = crypto_hash(timestamp, last_hash, data)
        return Block(timestamp, last_hash, hash, data)

    @staticmethod
    def genesis():
        return Block(**GENESIS_DATA)
    