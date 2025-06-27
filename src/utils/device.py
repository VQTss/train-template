import torch
import platform
from typing import Any
def get_device( logger,gpu=True):
    """
    
    """
    # CUDA (NVIDIA GPU) on Windows/Linux/Mac (with external GPU)
    logger.info(f"Load the device with function get_device")
    system = platform.system()
    if gpu and torch.cuda.is_available():
        device = torch.cuda.device("cuda")
        logger.info(f"Using {device} - System: {system}")
    elif gpu and torch.mps.is_available() and system == "Darwin" :
        device = torch.device("mps")
        logger.info(f"Using {device} - System: {system}")
    else:
        device = torch.device("cpu")
        logger.info(f"Using {device} - System: {system}")
    
    return device