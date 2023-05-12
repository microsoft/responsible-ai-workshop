import json
import numpy as np
import pandas as pd
import os
import onnxruntime as rt

def init():
    global onnx_session
    onnx_session = rt.InferenceSession(os.environ.get("MODEL_PATH"))

def run(request):
    try:
        df = pd.read_json(request)
        input_name = onnx_session.get_inputs()[0].name
        pred_onx = onnx_session.run(None, {input_name: df.to_numpy().astype(np.float32)})
        return {'data' : pred_onx[0].tolist() , 'message' : "Successfully classified loan"}
    except Exception as e:
        error = str(e)
        return {'data' : error , 'message' : "Failed to classify loan"}