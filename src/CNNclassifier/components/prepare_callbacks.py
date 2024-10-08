import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from CNNclassifier.entity.config_entity import PrepareCallbacksConfig

## doesnt need a pipeline as it is called in training hence not needed in main.py and dvc.yaml

class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config


    
    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_root_log_dir = str(self.config.tensorboard_root_log_dir)
        tb_running_log_dir = os.path.join(
            tb_root_log_dir,
            f"tb_logs_at_{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    

    @property
    def _create_ckpt_callbacks(self):
        # Convert Path object to string if necessary
        checkpoint_filepath = str(self.config.checkpoint_model_filepath)
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=checkpoint_filepath,
            save_best_only=True
        )


    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]