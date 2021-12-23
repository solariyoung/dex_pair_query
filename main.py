import web3


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


rpc = 'https://bsc-dataseed1.defibit.io'

# Press the green button in the gutter to run the script.
pancake_factory = '0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73'
gituar_factory = '0x99672E305FD27121D0dB389745D3aA8E26D73818'
biswap_factory = '0x858E3312ed3A876947EA49d572A7C42DE08af7EE'
bakery_factory = '0x01bF7C66c6BD861915CdaaE475042d3c4BaE16A7'
mdex_factory = '0x3CD1C46068dAEa5Ebb0d3f55F6915B10648062B8'
ape_factory = '0x0841BD0B734E4F5853f0dD8d7Ea041c241fb0Da6'

bsc_web3 = web3.Web3.HTTPProvider(rpc)
print(bsc_web3.isConnected())


