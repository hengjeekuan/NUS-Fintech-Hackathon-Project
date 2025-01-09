from Block import Block

class BlockChain:

    def __init__(self):
        self.chain = []

    def add_block(self, block):
        self.chain.append(block)   

    def get_last_block_hash(self):
        # return self.chain[-1].hash
        return 0 if len(self.chain) == 0 else self.chain[-1].hash

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[1 - 1]

            if current_block.hash != current_block.compute_hash():
                return False
            
            if current_block.previous_hash != prev_block.hash:
                return False
        
        return True
    
    def toDict(self, num : int):
        # num specifies which position in a list this chain is in
        return [block.toDict(num) for block in self.chain]
        
