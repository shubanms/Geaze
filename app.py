from fastapi import FastAPI
from logger import logger
from src.utils.utils import validateEthNodeConnection
from src.core.wallet import getWalletDetails
from src.models.dataModels import (
    helloWorldInputModel,
    walletAddressInputModel
)
from src.startUp.helloWorld import igniteApplication
from src.core.connector import web3

app = FastAPI()

logger.info("Application start-up successful!")

@app.post("/helloWorld/")
def helloWorld(inputData: helloWorldInputModel):
    helloWorldResponse = igniteApplication(inputData)
    return helloWorldResponse

@app.post("/connectWallet/")
def connectWallet(inputData: walletAddressInputModel):
    details = getWalletDetails(inputData)
    
    return details
