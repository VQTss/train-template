import logging
import os
from typing import Optional
from src.core.constants import Constants
import structlog

def get_logger(name:str,log_file: Optional[str] = None,level: str = "info"):
    """  """
    
    print(f"==>>>> Initialize the logging with the project {Constants.PROJECT_NAME} - version {Constants.VERSION}")
    # Prevent re-initialization
    if getattr(get_logger,"_is_configured", False):
        return structlog.get_logger(name)
    
    # Setup root logger 
    logging.basicConfig(level=level.upper())
    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S", utc=False),
        structlog.dev.set_exc_info,
    ]
    
    # console pretty printer (human-readable)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        structlog.stdlib.ProcessorFormatter(
                processor=structlog.dev.ConsoleRenderer(colors=True),
                foreign_pre_chain=processors
        )
    )
    
    handlers = [console_handler]
    
    # File handler append log in JSON file
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        file_handler = logging.FileHandler(log_file,mode='a')
        file_handler.setFormatter(
            structlog.stdlib.ProcessorFormatter(
                processor=structlog.processors.JSONRenderer(),
                foreign_pre_chain=processors
            )
        )
        handlers.append(file_handler)
    
    root_logger = logging.getLogger()
    root_logger.handlers = [] # Remove all handler first
    for h in handlers:
        root_logger.addHandler(h)
    
    root_logger.setLevel(level=level.upper())
    
    # Configure structlog
    structlog.configure(
        processors=processors + [
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    
    get_logger._is_configured = True
    
    return structlog.get_logger(name)
        
# Example
# logger = get_logger("train", log_file="outputs/logs/train.jsonl", level="info")
# logger.info("Training started!", step=0, loss=0.345)
# logger.warning("Something seems odd", batch=42)