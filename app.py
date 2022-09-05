# python program to create a simple blockchain

import datetime
import hashlib
import JSON
from flask import Flask, jsonify


class Blockchain:
    # This fuction will create the very first block and set its hash to 0
    def __init__(self):
        self.chain = None
        self.create_block(proof=1, previous_block='0')

    # Create a new block into the chain

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                'timestamp': str(datetime.datetime.now()),
                'proof': proof,
                'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    # display the hash of the previous block
    def print_previous_block(self, previous_proof):
        return self.chain[-1]
 
    # used for proof of work and used to successfully mine the block
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode())
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        