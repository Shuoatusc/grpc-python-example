import grpc
from concurrent import futures
import time
import logging

import TransferService_pb2
import TransferService_pb2_grpc

class TransferService(TransferService_pb2_grpc.TransferServiceServicer):
	def transfer(self, request, context):
		response = TransferService_pb2.TransferResponse(received_notice = "We received your info: %s."  %request)
		print(response)
		return response
	# def queryDB(info):
	# 	return
# Create a grpc server
def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	# Assign service to the server
	TransferService_pb2_grpc.add_TransferServiceServicer_to_server(TransferService(), server)
	print('Starting server. Listening on port 8080.')
	server.add_insecure_port('[::]:8080')
	server. start()
	try:
	    while True:
	        time.sleep(86400)
	except KeyboardInterrupt:
	    server.stop(0)

if __name__ == '__main__':
    logging.basicConfig()
    serve()
