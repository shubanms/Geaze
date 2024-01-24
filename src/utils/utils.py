from src.core.connector import web3
from logger import logger

def validateEthNodeConnection():
    if(web3.is_connected()):
        logger.info(f"Connection established to the ETH Node at {web3.eth.block_number}")
    else:
        logger.info("Connection to the ETH Node not established!")
