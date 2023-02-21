import pathlib
from typing import Optional
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing.text import tokenizer_from_json 
from keras.utils import pad_sequences
import numpy as np
from nbs.main import AIModel


class GrabModel() :
        AI_MODEL = None
        BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent #blog
        NBS_DIR = BASE_DIR / 'nbs'
        REVIEWS_DS_DIR = NBS_DIR / "reviews_dataset" 
        EXPORTS_DIR = REVIEWS_DS_DIR / "exports"
        MODEL_PATH = EXPORTS_DIR /"model.h5"
        TOKENIZER_PATH = EXPORTS_DIR /"tokenizer.json"
        METADATA_PATH = EXPORTS_DIR /"metadata.json"

        def __init__(self) :
            
            self.AI_MODEL = AIModel(
                model_path= self.MODEL_PATH ,
                tokenizer_path= self.TOKENIZER_PATH,
                metadata_path= self.METADATA_PATH
        
            )

         





