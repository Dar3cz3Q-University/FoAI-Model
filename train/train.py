import argparse
import pandas as pd
from pathlib import Path
from joblib import dump
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../cv_model/model.pkl")


def train_model(input_csv):
    print("Reading from: ", input_csv)

    df = pd.read_csv(input_csv)
    X = df["Resume"]
    y = df["Category"]

    print("Generating model...")

    model = Pipeline(
        [("tfidf", TfidfVectorizer()), ("clf", LogisticRegression(max_iter=1000))]
    )

    model.fit(X, y)

    print("Saving model...")

    dump(model, MODEL_PATH)

    print("Model saved!")


def main():
    parser = argparse.ArgumentParser(description="Train CV classifier model.")

    parser.add_argument(
        "input_csv", help="Path to input CSV file with 'text' and 'category' columns."
    )

    args = parser.parse_args()

    train_model(args.input_csv)


if __name__ == "__main__":
    main()
