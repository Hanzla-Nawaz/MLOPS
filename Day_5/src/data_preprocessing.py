import pandas as pd
import os
import logging
from nltk.stem.porter import PorterStemmer
import nltk
import string
from nltk.corpus import stopwords
from sklearn.preprocessing import LabelEncoder

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("data_ingestion")
logger.setLevel(logging.DEBUG)

if not logger.hasHandlers():
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    log_file = os.path.join(log_dir, "data_preprocessing.log")
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

def transform_text(text):
    """transform text to lowercase and remove special characters"""
    ps = PorterStemmer()
    text = text.lower()
    text = nltk.word_tokenize(text)
    text = [word for word in text if word.isalnum()]
    text = [word for word in text if word not in stopwords.words('english') and word not in string.punctuation]
    text = [ps.stem(word) for word in text]
    text = " ".join(text)
    return text

def preprocess_data(df, text_column = 'Message', label_column = 'Type'):
    try:
        encoder = LabelEncoder()
        df[label_column] = encoder.fit_transform(df[label_column])
        logger.debug(f"target column encoded successfully")
        df.drop_duplicates(inplace=True)
        logger.debug(f"duplicates dropped successfully")

        df.loc[:,text_column] = df[text_column].apply(transform_text)
        logger.debug(f"text column transformed successfully")
        return df   
    except Exception as e:
        logger.error(f"Failed to preprocess data: {e}")
        raise

def main(text_column = 'Message', label_column = 'Type'):
    """main function"""
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        train_df = pd.read_csv(os.path.join(base_dir, 'data', 'raw_data', 'train_data.csv'))
        test_df = pd.read_csv(os.path.join(base_dir, 'data', 'raw_data', 'test_data.csv'))
        train_df = preprocess_data(train_df, text_column, label_column)
        test_df = preprocess_data(test_df, text_column, label_column)
        data_path = os.path.join(base_dir, 'data', 'processed')
        os.makedirs(data_path, exist_ok=True)
        train_df.to_csv(os.path.join(data_path, "train.csv"), index=False)
        test_df.to_csv(os.path.join(data_path, "test.csv"), index=False)
        logger.info(f"Data preprocessed and saved to {data_path}")
    except Exception as e:
        logger.error(f"Failed to preprocess data: {e}")
        raise

if __name__ == "__main__":
    # Ensure NLTK resources are downloaded
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')
    main()


