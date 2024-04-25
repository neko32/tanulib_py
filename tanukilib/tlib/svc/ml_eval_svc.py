import grpc
from concurrent import futures
import tlib.svc.MLEvalService_pb2 as mlsvc_pb2
import tlib.svc.MLEvalService_pb2_grpc as mlsvc_grpc
from keras.models import Model, load_model
import os
from os.path import exists
from tlib.dateutil import cur_datetime_as_std_fmt_str
from tlib.math import sigmoid
from tlib.ml.img import load_img_as_1d
from tlib.ml.base import PREFERRED_IMG_SIZE_CATDOG


class MLEvalService(mlsvc_grpc.MLEvalServiceServicer):
    """Implements GRPC Service MLEvalService"""

    def __init__(self):
        self.model_cache = {}
    
    def Evaluate(self, req:mlsvc_pb2.MLEval, ctx):
        """Predict specified model with given input"""
        outcome = mlsvc_pb2.Outcome()
        print(req)

        # load model. If already exists in cache, get it from cache
        if req.model_name in self.model_cache:
            model:Model = self.model_cache[req.model_name]
        else:
            model_store_loc = os.path.join(os.environ["TANUAPP_ML_DIR"], "catdog")
            model:Model = load_model(model_store_loc)
            self.model_cache[req.model_name] = model
            if not exists(model_store_loc):
                outcome.code = 10001
                outcome.msg = "model dir doesn't exist"
                outcome.data = ""
                return outcome

        try:
            outcome.data = self.predict(
                model, 
                req.input.data[0].data_value, 
                req.input.data[1].data_value
            )
            outcome.code = 1
            outcome.msg = f"evaluated {model_store_loc} successfully"
        except Exception as e:
            outcome.code = 10000
            outcome.msg = str(e)

        return outcome
    
    def predict(self, model:Model, category_name:str, image_name:str) -> str:
        """Predict model with given category and image name"""
        img_siz = PREFERRED_IMG_SIZE_CATDOG

        img = load_img_as_1d(
            dataset_name="cat_and_dog/PetImages",
            category=category_name,
            file_name=image_name,
            size=img_siz
        )

        pred = model.predict(img)
        print(pred)
        raw_score = float(pred[0][0])
        score = sigmoid(raw_score)
        cat_per = f"{100 * (1 - score):.2f}"
        dog_per = f"{100 * score:.2f}% dog"
        result_str = f"{100 * (1 - score):.2f}% cat and {100 * score:.2f}% dog"
        cur_datestr = cur_datetime_as_std_fmt_str()

        print(f"score - {score}, raw score - {raw_score}")
        print(result_str)
        return result_str

class MLEvalServer():
    """Server to provide ML model evaluation"""

    def __init__(self):
        self.mlserver = MLEvalService()

    def start(self):
        """Start the server"""
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers = 5))
        mlsvc_grpc.add_MLEvalServiceServicer_to_server(self.mlserver, self.server)
        self.server.add_insecure_port("[::]:1234")
        self.server.start()
        self.server.wait_for_termination()

    def stop(self):
        """Stop the server"""
        self.server.stop(0)

if __name__ == "__main__":
    srv = MLEvalServer()
    srv.start()
