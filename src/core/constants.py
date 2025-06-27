import os


class Constants:
    PROJECT_NAME = os.getenv("PROJECT_NAME")
    VERSION = os.getenv("VERSION")
    LEVEL_LOGGER= os.getenv("LOG_LEVEL")
    PATH_CONFIG = os.getenv("PATH_CONFIG")
