import random
import csv
from blockChain import blockChain
from Block import block

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
        training_data_blockchain[j].add_block(block(curr["amount"], curr["transaction_type"], curr["login_frequency"],
                                                    curr["session_duration"], curr["purchase_pattern"], curr["age_group"], curr["anomaly"],
                                                    training_data_blockchain[j].get_last_block_hash() if k else training_data_blockchain[j].get_last_block_hash()[::-1]))
        
        curr = test_data[i]
        test_data_blockchain[j].add_block(block(curr["amount"], curr["transaction_type"], curr["login_frequency"],
                                                curr["session_duration"], curr["purchase_pattern"], curr["age_group"], curr["anomaly"],
                                                test_data_blockchain[j].get_last_block_hash() if k else test_data_blockchain[j].get_last_block_hash()[::-1]))
        
    
    return training_data_blockchain, test_data_blockchain

a, b = create_blockchains(data, 20, 0.00005, 10)

def create_dtl_dataset_from_blockchain(a, b):
    training_data_dict = []
    test_data_dict = []
    
    chains_that_were_tampered = []

    for i in range(len(a)):
        if not a[i].is_chain_valid():
            chains_that_were_tampered.append(a[i].chain)
            continue

        for j in range(len(a[i].chain)):
            training_data_dict.append(a[i].chain[j].toDict(i))

    for i in range(len(b)):
        if not b[i].is_chain_valid():
            chains_that_were_tampered.append(b[i].chain)
            continue

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

create_dtl_dataset_from_blockchain(a, b)