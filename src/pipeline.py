# Library
from dotenv import load_dotenv

# Load enviroment from .env file
load_dotenv()

# application
from src.core.config import load_config
from src.core.logger import get_logger
from utils.common import get_now_string
from src.core.constants import Constants
from src.utils.device import get_device

# time now
time_now = get_now_string()


# Logging
logger = get_logger(f"Train - version {Constants.VERSION}", f"outputs/logs/train_{Constants.VERSION}_{time_now}.jsonl")
logger.info("======= Start the pipeline ========")

device = get_device(logger=logger,gpu=True) # Just get the divices
 
config = load_config(path=Constants.PATH_CONFIG,logger=logger)

