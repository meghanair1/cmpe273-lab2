
from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = calculator_pb2_grpc.GreeterStub(channel)
  response = stub.Add(calculator_pb2.AddRequest(n1=50,n2=230))
  print("the sum of two numbers is :",response.n1)




if __name__ == '__main__':
    run()
