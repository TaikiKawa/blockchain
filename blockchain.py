import hashlib
import json


def calculate_hash(block):
    block_string = json.dumps(block).encode()
    return hashlib.sha256(block_string).hexdigest()



# 10行目と12行目を埋めてproof_of_workを実装してください
def proof_of_work(blockchain, previous_hash):
    nonce = 0
    while True:
        block = blockchain.create_block(nonce, previous_hash)
        # ブロックのハッシュ値を計算してください
        guess_hash = calculate_hash(block)
        #[:4]は前から4つの数が0000になるようなという意味．
        if guess_hash[:4] == "0000":
            break

        # pop()でリストの最も後ろにある要素を削除しています
        blockchain.chain.pop()
        nonce += 1
    return block
