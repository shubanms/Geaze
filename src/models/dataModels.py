from typing import Optional
from pydantic import BaseModel

class helloWorldInputModel(BaseModel):
    text: Optional[str] = " "
    
class helloWorldResponseModel(BaseModel):
    text: Optional[str] = " "

class walletAddressInputModel(BaseModel):
    walletAddress: Optional[str] = " "
    
class walletError(BaseModel):
    statusMessage: Optional[str] = "ERROR"

class walletData(BaseModel):
    walletAddress: Optional[str] = " "
    walletBalanceWEI: Optional[int] = 0
    walletBalanceETH: Optional[int] = 0
    walletTransactions: Optional[int] = 0
