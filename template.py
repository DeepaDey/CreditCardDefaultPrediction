import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="CreditCardDefaultPrediction"

list_of_files=[
    f"src/CreditCardDefaultPrediction/__init__.py",
    f"src/CreditCardDefaultPrediction/components/__init__.py",
    f"src/CreditCardDefaultPrediction/components/data_ingestion.py",
    f"src/CreditCardDefaultPrediction/components/data_transformation.py",
    f"src/CreditCardDefaultPrediction/components/model_trainer.py",
    f"src/CreditCardDefaultPrediction/components/model_monitering.py",
    f"src/CreditCardDefaultPrediction/pipelines/__init__.py",
    f"src/CreditCardDefaultPrediction/pipelines/training_pipeline.py",
    f"src/CreditCardDefaultPrediction/pipelines/prediction_pipeline.py",
    f"src/CreditCardDefaultPrediction/exception.py",
    f"src/CreditCardDefaultPrediction/logger.py",
    f"src/CreditCardDefaultPrediction/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file CreditCardDefaultPrediction")
        
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
            
        
    else:
        logging.info(f"CreditCardDefaultPrediction is already exists")