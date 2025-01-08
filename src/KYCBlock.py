import hashlib
from Block import Block

class KYCBlock(Block):
    def __init__(self, name, age, location, transactionHistory, 
                 balance, income, education, verified, prev_hash):
        self.name = name
        self.age = age
        self.location = location
        self.transactionHistory = transactionHistory
        self.balance = balance
        self.income = income
        self.education = education
        self.prev_hash = prev_hash
        self.verified= verified
        self.hash = self.computeHash()

    def compute_hash(self):
        block_string = f"{self.name}{self.age}{self.location}
                            {self.transaction_freq}{self.avg_transactionHistory}
                                {self.balance}{self.income}{self.education}
                                    {self.verified}{self.prev_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()
