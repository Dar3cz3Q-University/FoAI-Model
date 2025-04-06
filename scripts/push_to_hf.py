import os
from pathlib import Path
from huggingface_hub import upload_folder
from foai_model.logger import logger
from dotenv import load_dotenv

load_dotenv()

REPO_ID = "Dar3cz3Q/foai_model"
CHECKPOINT_DIR = Path("model") / "checkpoint-latest"


def push():
    token = os.getenv("HF_TOKEN")
    if not token:
        logger.error("HF_TOKEN environment variable not set.")
        exit(1)

    if not CHECKPOINT_DIR.exists():
        logger.error("Checkpoint folder not found: %s", CHECKPOINT_DIR)
        exit(1)

    logger.info("Uploading checkpoint to Hugging Face Hub...")

    upload_folder(
        repo_id=REPO_ID,
        folder_path=str(CHECKPOINT_DIR),
        path_in_repo="checkpoint",
        repo_type="model",
        token=token,
    )

    logger.info(
        "Checkpoint uploaded to: https://huggingface.co/%s/tree/main/checkpoint",
        REPO_ID,
    )
