import keras
from keras.models import Model
from keras.layers import Input, Dense
from keras.optimizers import SGD
import tensorflow as tf
from typing import List, Any

class ModelBuilder:
    def __init__(self, ipt_shape:List[Any]):
        self.input = Input(shape = ipt_shape)
        self.output = None
        self.model_buf = self.input
    
    def set_output(self, units:int, activation:str) -> None:
        self.output = Dense(units = units, activation = activation)(self.model_buf)
        
    def build(self) -> Model:
        return Model(inputs = self.input, outputs = self.output)

def get_available_gpu_devices() -> bool:
    return tf.config.list_physical_devices('GPU')

def gen_default_SGD(lr:float = 0.01) -> SGD:
    return SGD(learning_rate = lr)
