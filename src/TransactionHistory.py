import numpy as np
import time
import datetime

class TransactionHistory: 
    def __init__(self, array):
        self.array = array

    def add_transaction(self, date, amount):
        self.array = self.array.append((date, amount))

    def avg_transaction_amt(self):
        return np.mean(np.array(self.array), axis = 0)[-1]
    
    def transactions_in_last_24_hours(self):
        unix_timestamp = int(time.time()/86400)
        return len(list(filter(lambda x : x[0] >= unix_timestamp - 1, self.array)))    

    