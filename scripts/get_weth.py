from scripts.helpful_scripts import get_account
from brownie import network, interface,config
from web3 import Web3
def main():
    get_weth()

def get_weth():
    """
    Mints WETH by depositing ETH
    """
    account = get_account()
    value = 0.1
    weth = interface.IWeth(config["networks"][network.show_active()]["weth-token"])
    tx = weth.deposit({"from": account,"value": value*10**18})
    tx.wait(1)
    print (f"Received {value} WETH")
    return tx