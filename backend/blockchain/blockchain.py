from backend.blockchain.block import Block

class Blockchain:

    def __init__(self):
        self.chain = [Block.genesis()]
    
    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))
    
    def __repr__(self) -> str:
        return f'Bloackchain: {self.chain}'
    
def main():
    blockchain = Blockchain()
    blockchain.add_block("one")
    blockchain.add_block(2)
    blockchain.add_block([3])
    print(blockchain)

if __name__ == "__main__":
    main()
