import logging, os

def setUpLogging():
    logs_dir = 'logs'
    os.makedirs(logs_dir, exist_ok=True)

    logging.basicConfig(
        filename=os.path.join(logs_dir, 'app.log'),
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

setUpLogging()

logger = logging.getLogger(__name__)
