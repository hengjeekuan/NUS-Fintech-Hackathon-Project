import hashlib

class block:
    def __init__(self, amount, txn_type, login_freq, sess_dur, pattern, age, anomaly, prev_hash):
        self.amount = amount
        self.txn_type = txn_type
        self.login_freq = login_freq
        self.sess_dur = sess_dur
        self.pattern = pattern
        self.age = age
        self.anomaly = anomaly
        self.hash = self.computeHash()
        self.prev_hash = prev_hash

    def computeHash(self):
        a = f"{self.amount}{self.txn_type}{self.login_freq}{self.sess_dur}{self.pattern}{self.age}"
        return hashlib.sha256(a.encode()).hexdigest()
    
    def toDict(self, num : int):
        return {
            "amount": self.amount,
            "txn_type" : self.txn_type,
            "login_freq" : self.login_freq,
            "sess_dur" : self.sess_dur,
            "pattern" : self.pattern,
            "age" : self.age,
            "anomaly" : self.anomaly
        }