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