from cnnClassifier.pipeline.stage_01_dataIngestion import DataIngestionTrainingPipeline
from cnnClassifier import logger


STAGE_NAME="DataIngestion"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_training_pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
