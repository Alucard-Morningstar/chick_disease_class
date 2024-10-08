from CNNclassifier import logger
from CNNclassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNclassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline





## Delete the artifacts folder if rerunning the pipeline
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e



## Run seperately if data ingestion is already done
STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e