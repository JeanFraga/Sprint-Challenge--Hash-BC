import hashlib
import requests

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last five digits of hash(p) are equal
    to the first five digits of hash(p')
    - IE:  last_hash: ...AE912345, new hash 12345888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()

    print("Searching for next proof")
    proof = random.random()
    #  TODO: Your code here
    block_string = f'{last_proof}'.encode()
    hash_obj = hashlib.sha256(block_string).hexdigest()
    while not valid_proof(hash_obj, proof):
        proof += random.random()
    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last five characters of
    the hash of the last proof match the first five characters of the hash
    of the new proof?

    IE:  last_hash: ...AE912345, new hash 12345E88...
    """

    guess = f"{proof}".encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:5] == last_hash[-5:]


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))

# ID is JeanFraga

# Searching for next proof
# Proof found: 2124391.3118945244 in 6.6454989459998615
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 536873.9037797035 in 1.7549770699988585
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 645913.6758688051 in 1.8801686059996428
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 450671.80053912447 in 1.3972689829988667
# Total coins mined: 1
# Searching for next proof
# Proof found: 88351.81222528008 in 0.3111892340002669
# Total coins mined: 2
# Searching for next proof
# Proof found: 173418.91574814433 in 0.5792458949999855
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 33963.15617533323 in 0.1065860890012118
# Total coins mined: 3
# Searching for next proof
# Proof found: 279086.6816899932 in 0.8444029010006489
# Total coins mined: 4
# Searching for next proof
# Proof found: 367427.3121130526 in 1.282102693001434
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 449117.6062269769 in 1.4687286780008435
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 379922.6557013784 in 1.2978879109996342
# Total coins mined: 5
# Searching for next proof
# Proof found: 284205.04129433463 in 0.9594986160009285
# Total coins mined: 6
# Searching for next proof
# Proof found: 26586.743532491266 in 0.11247607900077128
# Total coins mined: 7
# Searching for next proof
# Proof found: 351432.8587309231 in 1.2442341799996939
# Total coins mined: 8
# Searching for next proof
# Proof found: 79652.51385003162 in 0.27835656800016295
# Total coins mined: 9
# Searching for next proof
# Proof found: 346380.9643883693 in 1.0671206429997255
# Total coins mined: 10
# Searching for next proof
# Proof found: 118827.63620004468 in 0.3686927119997563
# Total coins mined: 11
# Searching for next proof
# Proof found: 44091.057436203286 in 0.13781156000004557
# Total coins mined: 12
# Searching for next proof
# Proof found: 529261.0341669845 in 1.6239523899985215
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 609073.7133811697 in 2.0088496770003985
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 153806.17498481963 in 0.44593424199956644
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 440797.0551223602 in 1.354337996999675
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 198481.5284393274 in 0.6250914619995456
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 310493.773711919 in 0.9064520369993261
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 54648.300683878726 in 0.19683546399937768
# Total coins mined: 13
# Searching for next proof
# Proof found: 566874.582673261 in 1.9745622589998675
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 107423.57369027409 in 0.36311156100055086
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 259121.86224099394 in 0.9870520679996844
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 1738513.059523235 in 5.672596260999853
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 453430.3212934941 in 1.4038921989995288
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 331101.37356612855 in 1.0564621680005075
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 275837.95042312116 in 0.9756728939992172
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 164905.1585694081 in 0.578101097000399
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 50482.48780656466 in 0.18851868800084048
# Total coins mined: 14
# Searching for next proof
# Proof found: 66074.32477453243 in 0.25301028799913183
# Total coins mined: 15
# Searching for next proof
# Proof found: 497423.3406448127 in 1.7598071540014644
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 299494.9170285707 in 1.0579729509991012
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 1940339.994383817 in 5.999103881998963
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 177690.52869790682 in 0.5930075539999962
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 50031.561335451166 in 0.16027170100096555
# Total coins mined: 16
# Searching for next proof
# Proof found: 224041.64402896358 in 0.6859757199999876
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 1175400.011058112 in 3.607013447999634
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 345791.2305841285 in 1.1288982730002317
# Total coins mined: 17
# Searching for next proof
# Proof found: 1048984.270391471 in 3.021053288000985
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 112440.37855737943 in 0.38666929499959224
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 497772.29151071166 in 1.597651288000634
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 1830279.207523759 in 5.693332415999976
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 420768.56210850837 in 1.3945169999988138
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 98247.82476217131 in 0.3273818800007575
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 723694.2329533771 in 2.2260038900003565
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 294930.3162649952 in 0.940870783999344
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 353065.31977326307 in 1.2118687729998783
# Proof valid but already submitted.
# Searching for next proof
# Proof found: 763286.5282684843 in 2.3175663929996517
# Proof valid but already submitted.
# Searching for next proof