import grpc
from concurrent import futures
import time
import os
import django

from grpc_reflection.v1alpha import reflection

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoGRPC.settings")
django.setup()

import book_pb2
import book_pb2_grpc
from library.services import BookService

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Register your service
    book_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)

    # Enable reflection
    SERVICE_NAMES = (
        book_pb2.DESCRIPTOR.services_by_name['BookService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server running on port 50051 with reflection...")
    
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
