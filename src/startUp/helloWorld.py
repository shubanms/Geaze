from src.models.dataModels import helloWorldInputModel, helloWorldResponseModel
from logger import logger

def igniteApplication(inputData: helloWorldInputModel):
    response = helloWorldResponseModel()
    response.text = inputData.text
    
    logger.info(f'Response text is {response.text}')
    
    return response
