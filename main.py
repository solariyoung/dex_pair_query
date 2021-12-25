import random

from web3 import Web3

import abi

file = open("./pairs.txt", mode='w')

def pair_add(pair):
    if pair[0] == "Cake-LP":
        pancake_pair.append(pair)
    if pair[0] == "Guitar-LP":
        guitar_pair.append(pair)
    if pair[0] == "BSW-LP":
        biswap_pair.append(pair)
    if pair[0] == "BLP":
        bakery_pair.append(pair)
    if pair[0] == "MDEXLP":
        mdex_pair.append(pair)
    if pair[0] == "APE-LP":
        ape_pair.append(pair)
    file.write(str(pair))
    file.write('\n')

    if random.randint(1, 20) == 1:
        file.flush()


rpc = 'https://bsc-dataseed1.defibit.io'

# Press the green button in the gutter to run the script.
pancake_factory = '0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'
guitar_factory = '0x99672E305FD27121D0dB389745D3aA8E26D73818'
biswap_factory = '0x858E3312ed3A876947EA49d572A7C42DE08af7EE'
bakery_factory = '0x01bF7C66c6BD861915CdaaE475042d3c4BaE16A7'
mdex_factory = '0x3CD1C46068dAEa5Ebb0d3f55F6915B10648062B8'
ape_factory = '0x0841BD0B734E4F5853f0dD8d7Ea041c241fb0Da6'

bsc_web3 = Web3(Web3.HTTPProvider(rpc))
print(bsc_web3.isConnected())

# factory contract init
pancake = bsc_web3.eth.contract(address=pancake_factory, abi=abi.factory_abi)
guitar = bsc_web3.eth.contract(address=guitar_factory, abi=abi.factory_abi)
biswap = bsc_web3.eth.contract(address=biswap_factory, abi=abi.factory_abi)
bakery = bsc_web3.eth.contract(address=bakery_factory, abi=abi.factory_abi)
mdex = bsc_web3.eth.contract(address=mdex_factory, abi=abi.factory_abi)
ape = bsc_web3.eth.contract(address=ape_factory, abi=abi.factory_abi)

factory_list = [pancake, guitar, biswap, bakery, mdex, ape]

pancake_pair = []
guitar_pair = []
biswap_pair = []
bakery_pair = []
mdex_pair = []
ape_pair = []


for f in factory_list:
    pairs_num = f.functions.allPairsLength().call()

    p = 212600
    while p < pairs_num:
        print(p)
        pair = f.functions.allPairs(p).call()

        lp = bsc_web3.eth.contract(address=pair, abi=abi.lp_abi)
        reserves = lp.functions.getReserves().call()

        if reserves[0] > 10 * 1e18 and reserves[1] > 10 * 1e18:
            lp_name = lp.functions.symbol().call()
            token0_address = lp.functions.token0().call()
            token1_address = lp.functions.token1().call()

            try:
                token0_symbol = bsc_web3.eth.contract(address=token0_address, abi=abi.token_abi).functions.symbol().call()
                token1_symbol = bsc_web3.eth.contract(address=token1_address, abi=abi.token_abi).functions.symbol().call()
            except:
                p += 1
                continue

            print(lp_name, token0_symbol, token0_address, token1_symbol, token1_address)
            pair_to_collect = [lp_name,
                               [token0_symbol, token1_symbol],
                               [token0_address, token1_address]
                               ]
            pair_add(pair_to_collect)

        p += 1

file.close()

