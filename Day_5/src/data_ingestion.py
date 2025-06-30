import pandas as pd
import os
from sklearn.model_selection import train_test_split
import logging

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# logging levels
'''
DEBUG - Detailed information, typically for developers
INFO - General information about system operation
WARNING - Potentially harmful situations
ERROR - Serious errors that prevent the system from functioning
CRITICAL - Critical errors that may lead to system failure
'''

logger = logging.getLogger("data_ingestion")
logger.setLevel(logging.DEBUG)

if not logger.hasHandlers():
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    log_file = os.path.join(log_dir, "data_ingestion.log")
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

def load_data(data_url: str) -> pd.DataFrame:
    """load data from a csv file"""
    try:
        df = pd.read_csv(data_url, sep='\t')
        logger.debug(f"Data loaded successfully from {data_url}")
        return df
    except Exception as e:
        logger.error(f"Failed to load data from {data_url}: {e}")
        raise

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """preprocess the data"""
    try:
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        df.reset_index(drop=True, inplace=True)
        logger.debug("Data preprocessed successfully")
        return df
    except Exception as e:
        logger.error(f"Failed to preprocess data: {e}")
        raise

def save_data(df: pd.DataFrame, save_dir: str) -> None:
    """save the data to a csv file"""
    try:
        save_dir = os.path.join(save_dir, "raw_data")
        os.makedirs(save_dir, exist_ok=True)
        train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)
        train_data.to_csv(os.path.join(save_dir, "train_data.csv"), index=False)
        test_data.to_csv(os.path.join(save_dir, "test_data.csv"), index=False)
        logger.debug(f"Data saved successfully to {save_dir}")
    except Exception as e:
        logger.error(f"Failed to save data: {e}")
        raise

def main():
    """main function"""
    try:
        data_url = "https://raw.githubusercontent.com/bigmlcom/python/refs/heads/master/data/spam.csv"
        df = load_data(data_url)
        df = preprocess_data(df)
        save_data(df, 'data')  # Save train and test splits
        logger.info("Data ingestion completed successfully")
    except Exception as e:
        logger.error(f"Error in main function: {e}")
        raise

if __name__ == "__main__":
    main()

