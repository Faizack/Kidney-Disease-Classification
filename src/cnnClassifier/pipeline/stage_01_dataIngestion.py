from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.dataingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME="DataIngestion"

class DataIngestionTrainingPipeline :
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            logger.info("DataIngestion successfully")
        except Exception as e:
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_training_pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


