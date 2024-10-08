## Updating the configuration file with the data ingestion related configuration entities or custom return types

from dataclasses import dataclass
from pathlib import Path



## creating an entity i.e, a custom return type using entity
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModeConfig:
    root_dir: Path       #comes from config
    base_model_path : Path    #comes from config
    updated_base_model_path: Path       #comes from config
    params_image_size: list     #comes from params
    params_learning_rate: float  #comes from params
    params_include_top: bool     #comes from params
    params_weights: str         #comes from params
    params_classes: int         #comes from params



@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list