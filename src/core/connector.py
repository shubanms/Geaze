from web3 import Web3
import configs
from logger import logger

def connectToWeb3():
    web3 = Web3(Web3.HTTPProvider(configs.infuriaNodeApiKey))
    
    logger.info("Connection to Infuria established!")
    
    return web3

web3 = connectToWeb3()
