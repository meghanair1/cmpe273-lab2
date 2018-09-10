
from concurrent import futures
import time

import grpc

import calculator_pb2
import calculator_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(calculator_pb2_grpc.GreeterServicer):

    def Add(self, request, context):
      return calculator_pb2.AddReply(n1=request.n1 + request.n2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
