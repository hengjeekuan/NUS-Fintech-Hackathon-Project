import numpy as np
import time
import datetime

class TransactionHistory: 
    def __init__(self, array):
        self.array = array

    def add_transaction(self, date, amount):
        self.array = self.array.append((date, amount))

    def avg_transaction_amt(self):
        return np.mean(np.array(self.array)[:1])
    
    def transactions_in_last_24_hours(self):
        unix_timestamp = (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds()
        return list(filter(lambda x : x > unix_timestamp - 60*60*24, self.array)).count()
        

    