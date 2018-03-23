# 前回の実装内容をここで導入しています
from blockchain import proof_of_work, calculate_hash
import time




class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.transaction_index = 0
        # トランザクションにコインベースを追加します
        self.create_transaction(sender='0', recipient="my_address", amount=1)
        proof_of_work(self, previous_hash = "00000")

#以下で1blockに収納されているものを記述+blockchainに追加
    def create_block(self, nonce, previous_hash):
        block = {
            'index' : len(self.chain),
            'timestamp' : time.time(),
            'transactions' : self.current_transactions,
            'nonce' : nonce,
            'previous_hash' : previous_hash,
        }
        self.chain.append(block)
        return block

    def create_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'transaction_index' : self.transaction_index,
            'sender' : sender,
            'recipient' : recipient,
            'amount' : amount,
            })
        self.transaction_index += 1
        return self.transaction_index, len(self.chain)
#Object生成
blockchain = Blockchain()


def mine(blockchain):
    # 直前のブロックのハッシュ値を計算．リストの[-1]は最後の要素という意味．
    previous_hash = calculate_hash(blockchain.chain[-1])
    # proof_of_work関数を用いて、新しくブロックをマイニングしてください
    proof_of_work(blockchain, previous_hash)
    # current_transactionsとtransaction_indexを初期化してください
    blockchain.current_transactions = []
    blockchain.transaction_index = 0
    # current_transactionsにコインベースを追加しています
    blockchain.create_transaction(sender='0', recipient="my_address", amount=1)
    blockchain.create_transaction(sender='0', recipient="my_address", amount=1)
    block = blockchain.chain[-1]

    # 新しいブロックの情報をresponseに代入しています
    response = {
        'message': '新しいブロックを採掘しました',
        'index': block['index'],
        'nonce': block['nonce'],
        'previous_hash': block['previous_hash'],
    }
    return response

print(mine(blockchain))

#blockchainのinstanceには．blockのdic配列が収納されるchain配列と，blockごとにtransactionを毎回初期化して入れられるcurrent_transaction配列が用意されている．
#Blockchain.chainの中身は．blockの辞書型配列がappendされているので以下のような形のものが入っている．混乱の原因は，リストの中に二次元配列が含まれているから．
#[{'index': 0, 'timestamp': 1521303425.8742678, 'nonce': 5555, 'previous_hash': 7777}, {'index': 1, 'timestamp': 1521303525.579255, 'nonce': 2222, 'previous_hash': 9999}]
