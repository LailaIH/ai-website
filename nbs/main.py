from pathlib import Path
from dataclasses import dataclass
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing.text import tokenizer_from_json
from typing import Optional,List
import json 
from keras.utils import pad_sequences
import numpy as np
from. import encoder 

@dataclass
class AIModel:
    model_path : Path
    tokenizer_path : Optional[Path] = None
    metadata_path : Optional[Path] = None
    model=None
    tokenizer=None
    metadata=None

    def __post_init__(self):
        if self.model_path.exists():
            self.model = load_model(self.model_path)

        if self.tokenizer_path:
                if self.tokenizer_path.exists():
                    if self.tokenizer_path.name.endswith('json'):
                        tokenizer_text = self.tokenizer_path.read_text()
                        self.tokenizer = tokenizer_from_json(tokenizer_text)

        if self.metadata_path:
                if self.metadata_path.exists():
                    if self.metadata_path.name.endswith('json'):
                        self.metadata = json.loads(self.metadata_path.read_text())


    def get_model(self):
        if not self.model:
            raise Exception("Model not Implemented")
        return self.model 


    def get_tokenizer(self):
        if not self.tokenizer:
            raise Exception("Tokenizer not Implemented")
        return self.tokenizer 


    def get_metadata(self):
        if not self.metadata:
            raise Exception("Metadata not Implemented")
        return self.metadata       



    def get_sequences_from_text(self , texts:List[str])  :
        tokenizer  = self.get_tokenizer()
        sequences = tokenizer.texts_to_sequences(texts)
        return sequences
               

    def get_input_from_sequences(self,sequences):
        maxlen = self.get_metadata().get('max_sequence') or 280
        X_input = pad_sequences(sequences , maxlen=maxlen)
        return X_input


    def get_label_legend_inverted(self):
        legend = self.get_metadata().get("labels_legend_inverted") or{}
        if len(legend.keys()) != 2 :
            raise Exception("legend is incorrect")

        return legend  


    def get_label_pred(self,idx,val):
        legend = self.get_label_legend_inverted()
        return {"label": legend[str(idx)] , "confidence" : val}


    def get_top_pred_labeled(self,preds):
        top_idx_val = np.argmax(preds)    #returns the index of the max element
        val = preds[top_idx_val]
        return self.get_label_pred(top_idx_val , val)



    def predict_text(self,query:str , include_top=True , encode_to_json=True):
        model = self.get_model()
        sequences = self.get_sequences_from_text([query])
        X_input = self.get_input_from_sequences(sequences)
        preds = model.predict(X_input)[0]
        labeled_preds = [self.get_label_pred(i,x) for i,x in enumerate(list(preds))]

       

        results = {"predictions" : labeled_preds}

        if include_top:
            results['top'] = self.get_top_pred_labeled(preds)

        if encode_to_json:
           return encoder.encode_to_json(results , as_py=True)







