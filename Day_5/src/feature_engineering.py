import os
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Set up logger
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("feature_engineering")
logger.setLevel(logging.DEBUG)

if not logger.hasHandlers():
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    log_file = os.path.join(log_dir, "feature_engineering.log")
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

def tfidf_vectorizer(df, text_column='Message', max_features=500):
    """
    Fit a TfidfVectorizer on the specified text column of the DataFrame.
    Returns the fitted vectorizer.
    """
    try:
        # Drop rows with missing text
        df = df.dropna(subset=[text_column])
        vectorizer = TfidfVectorizer(max_features=max_features)
        vectorizer.fit(df[text_column])
        logger.debug("Vectorizer fitted successfully.")
        return vectorizer
    except Exception as e:
        logger.error(f"Failed to fit vectorizer: {e}")
        raise

def transform_and_save(df, vectorizer, text_column, output_path):
    """
    Transform the text column using the provided vectorizer and save as CSV.
    """
    try:
        # Drop rows with missing text
        df = df.dropna(subset=[text_column])
        X = vectorizer.transform(df[text_column])
        feature_names = vectorizer.get_feature_names_out()
        X_df = pd.DataFrame(X.toarray(), columns=feature_names)
        X_df.to_csv(output_path, index=False)
        logger.info(f"Transformed data saved to {output_path}")
    except Exception as e:
        logger.error(f"Failed to transform or save data: {e}")
        raise

def main(text_column='Message', train_file='train.csv', test_file='test.csv'):
    """
    Main function to perform TF-IDF feature engineering on train and test data.
    """
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, 'data', 'processed')
        train_path = os.path.join(data_dir, train_file)
        test_path = os.path.join(data_dir, test_file)
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)
        vectorizer = tfidf_vectorizer(train_df, text_column)
        logger.info("Vectorizer fitted successfully.")
        # Transform and save
        transform_and_save(train_df, vectorizer, text_column, os.path.join(data_dir, 'train_tfidf.csv'))
        transform_and_save(test_df, vectorizer, text_column, os.path.join(data_dir, 'test_tfidf.csv'))
        logger.info("Feature engineering completed successfully.")
    except Exception as e:
        logger.error(f"Feature engineering failed: {e}")
        raise

if __name__ == "__main__":
    main()