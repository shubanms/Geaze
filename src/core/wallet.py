from src.core.connector import web3
from logger import logger
from src.models.dataModels import walletAddressInputModel, walletError, walletData

def getWalletDetails(inputData: walletAddressInputModel):
    if not web3.is_address(inputData.walletAddress):
        error = walletError()
        return error
    
    walletDataResponse = walletData()
    
    walletDataResponse.walletBalanceWEI = web3.eth.get_balance(inputData.walletAddress)
    walletDataResponse.walletBalanceETH = web3.from_wei(walletDataResponse.walletBalanceWEI, 'ether')
    walletDataResponse.walletTransactions = web3.eth.get_transaction_count(inputData.walletAddress)
    walletDataResponse.walletAddress = inputData.walletAddress
    
    return walletDataResponse
