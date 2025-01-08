import hashlib
import time
from Block import Block

class ContractBlock(Block):
    def __init__(self, sender, receiver, amount, start_loc, end_loc, prev_hash):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.prev_hash = prev_hash
        self.hash = self.computeHash()

        def compute_hash(self):
            block_string = f"{self.sender}{self.receiver}{self.amount}{self.prev_hash}"
            return hashlib.sha256(block_string.encode()).hexdigest()
