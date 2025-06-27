import yaml
import json
import argparse
from src.core.constants import Constants

class Config(dict):

    def __getattr__(self, name):
        return self[name]
    
    def __setattr__(self, name):
        return self[name]
    
def load_config(logger,path:str) -> Config:
    """ 
    Load YAML or JSON config file into a dot-access dict
    """
    logger.info("Load of config path with function load_config", path=path)
    if path.endswith('.yaml') or path.endswith('.yml'):
        with open(path,'r') as f:
            cfg = yaml.safe_load(f)
    elif path.endswith('.json'):
        with open(path,'r') as f:
            cfg = json.load(f)
    else:
        raise ValueError(f"Unsupported cofig format {path}")
    
    logger.critical("Data of config", data=cfg)
    return Config(cfg)


def parse_args():
    """
    Use argparse to override config settings via command-line.
    """
    
    parser = argparse.ArgumentParser(description=f"{Constants.PROJECT_NAME} - {Constants.VERSION} Config")
    parser.add_argument('--config_path', type=str,required=True,help="Path to config file")
    # add more config if you need
    
    args = parser.parse_args()
    config = load_config(args)
    
    return config


# Usage

# config = load_config("configs/json/cfg_train.json") # Load JSON
# config = load_config("configs/yaml/cfg_train.yaml") # Load YAML
# train_images = config.DATA_DIR_TRAIN_IMAGES
# label_csv = config.DATA_DIR_TRAIN_LABEL
# image_size = config.IMAGE_SIZE
# num_classes = config.NUM_CLASSES
# batch_size = config.BATCH_SIZE
# means = config.PRETRAINED_MEANS


# print("Train Images Path:", train_images)
# print("Label CSV Path:", label_csv)
# print("Image Size:", image_size)
# print("Number of Classes:", num_classes)
# print("Batch Size:", batch_size)
# print("Pretrained Means:", means)