
# ⛓️Blockchain using Python

This web app helps you usnderstand the working of blockchain. Cover the basic concepts of mining, cryptography, hashing and decentralization.


## 🪛Installation

How to run project:

```
https://github.com/vishalsingh17/BlockchainUsingPython
```
```
cd BlockchainUsingPython
```
```
conda create -p venv python==3.7
```
```
conda activate ./venv
```
```
pip install -r requirements.txt
```
```
python app.py
```
## 👨‍💻Tech Stack

1. Python
2. Flask
3. JSON
4. Hashlib




## ✍🏻Acknowledgements

 - [Blockchain Wiki](https://en.wikipedia.org/wiki/Blockchain#:~:text=A%20blockchain%20is%20a%20decentralized,alteration%20of%20all%20subsequent%20blocks.)
 - [Official Blockchain Website](https://www.blockchain.com/)


## FAQ

#### Q1. What is Blockchain?

Ans1. A blockchain is a time-stamped decentralized series of fixed records that contains data of any size is controlled by a large network of computers that are scattered around the globe and not owned by a single organization. Every block is secured and connected with each other using hashing technology which protects it from being tampered by an unauthorized person. 

#### Q2. Project explanation.

Ans2. Creating Blockchain using Python, mining new blocks, and displaying the whole blockchain: 

- The data will be stored in JSON format which is very easy to implement and easy to read. The data is stored in a block and the block contains multiple data. Each and every minute multiple blocks are added and to differentiate one from the other we will use fingerprinting.
- The fingerprinting is done by using hash and to be particular we will use the SHA256 hashing algorithm. Every block will contain its own hash and also the hash of the previous function so that it cannot get tampered with.
- This fingerprinting will be used to chain the blocks together. Every block will be attached to the previous block having its hash and to the next block by giving its hash.
- The mining of the new block is done by giving successfully finding the answer to the proof of work. To make mining hard the proof of work must be hard enough to get exploited.
- After mining the block successfully the block will then be added to the chain.
- After mining several blocks the validity of the chain must be checked in order to prevent any kind of tampering with the blockchain.
- Then the web app will be made by using Flask and deployed locally or publicly as per the need of the user.

