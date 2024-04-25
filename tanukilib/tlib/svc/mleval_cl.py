import grpc
import tlib.svc.MLEvalService_pb2 as mlsvc_pb2
import tlib.svc.MLEvalService_pb2_grpc as mlsvc_grpc

def main():

    req = mlsvc_pb2.MLEval()
    ipt_data1 = mlsvc_pb2.Data(data_value = "Cat", data_type = "str")
    ipt_data2 = mlsvc_pb2.Data(data_value = "37.jpg", data_type = "str")
    ipt = mlsvc_pb2.InputData(data_path = "NA", data = [ipt_data1, ipt_data2])
    req = mlsvc_pb2.MLEval(model_name = "catdog", input = ipt)

    with grpc.insecure_channel("localhost:1234") as channel:
        stub = mlsvc_grpc.MLEvalServiceStub(channel)
        resp = stub.Evaluate(req)

    print(resp)

if __name__ == "__main__":
    main()
