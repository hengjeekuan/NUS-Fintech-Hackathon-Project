import random
import csv
from blockChain import blockChain
from block import block
import json

with open("src/metaverse_transactions_dataset.csv", 'r', newline='') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]


def create_blockchains(dataset, numOfBlockChains : int, failedHashRate : float = 0, seed: int = 2):
    # splits data into 2 sets (training and test)
    random.seed(seed)
    
    training_data = []
    test_data = []

    for i in range(len(dataset)):
        if random.randint(0, 1) == 0:
            training_data.append(dataset[i])
        else:
            test_data.append(dataset[i])
        
        if len(training_data) < len(dataset) / 2 and len(test_data) == len(dataset) / 2:
            for j in range(i + 1, len(dataset)):
                training_data.append(dataset[j])
            break

        if len(test_data) < len(dataset) / 2 and len(training_data) == len(dataset) / 2:
            for j in range(i + 1, len(dataset)):
                test_data.append(dataset[j])
            break
    
    training_data_blockchain = []
    test_data_blockchain = []

    for i in range(numOfBlockChains):
        training_data_blockchain.append(blockChain())
        test_data_blockchain.append(blockChain())

    for i in range(len(training_data)):
        j = random.randint(0, numOfBlockChains - 1)
        k = random.random() >= failedHashRate
        
        curr = training_data[i]
        training_data_blockchain[j].add_block(block(categorise_amount(curr["amount"]), curr["transaction_type"], categorise_login_freq(curr["login_frequency"]),
                                                    categorise_session_dur(curr["session_duration"]), curr["purchase_pattern"], curr["age_group"], curr["risk_score"],
                                                    curr["anomaly"],
                                                    training_data_blockchain[j].get_last_block_hash() if k else training_data_blockchain[j].get_last_block_hash()[::-1]))
        
        curr = test_data[i]
        test_data_blockchain[j].add_block(block(categorise_amount(curr["amount"]), curr["transaction_type"], categorise_login_freq(curr["login_frequency"]),
                                                categorise_session_dur(curr["session_duration"]),
                                                curr["purchase_pattern"], curr["age_group"], curr["risk_score"], curr["anomaly"],
                                                test_data_blockchain[j].get_last_block_hash() if k else test_data_blockchain[j].get_last_block_hash()[::-1]))
        
    
    return training_data_blockchain, test_data_blockchain

 
def categorise_amount(amt):
    amt = float(amt)
    if amt < 500:
        return "amt < 500"
    elif amt < 1000:
        return "500 <= amt < 1000"
    else:
        return "amt >= 1000"
    
def categorise_login_freq(freq):
    freq = int(freq)
    if freq <= 2:
        return "freq <= 2"
    elif freq <= 4:
        return "2 < freq <= 4"
    elif freq <= 6:
        return "4 < freq <= 6"
    else:
        return ">= 6"
    
def categorise_session_dur(time):
    time = int(time)
    if time <= 40:
        return "time <= 40"
    elif time <= 80:
        return "40 < time <= 80"
    elif time <= 120:
        return "80 < time <= 120"
    else:
        return ">= 120"

a, b = create_blockchains(data, 20, 0.01, 10)

training_data_dict = []
test_data_dict = []

for i in range(len(a)):
    for j in range(len(a[i].chain)):
        training_data_dict.append(a[i].chain[j].toDict(i))

for i in range(len(b)):
    for j in range(len(b[i].chain)):
        test_data_dict.append(b[i].chain[j].toDict(i))


with open("src/training_dataset.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=training_data_dict[0].keys())
    writer.writeheader()
    writer.writerows(training_data_dict)

with open("src/test_dataset.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=test_data_dict[0].keys())
    writer.writeheader()
    writer.writerows(test_data_dict)