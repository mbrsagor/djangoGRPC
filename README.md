# Django gRPC

> Django gRPC refers to the use of the gRPC framework within a Django application. gRPC (Google Remote Procedure Call) is a high-performance, open-source framework for building APIs.

##### Setup:

> The following steps will walk you through installation on a Mac. Linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed Django apps on Windows, you should have little problem getting up and running.

#### Dependencies

- Python 3.12
- Rest framework
- django_grpc_framework

#### Install project locally:
```bash
git clone https://github.com/mbrsagor/djangoGRPC.git
cd djangoGRPC
virtualenv venv --python=python3.12
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
```

#### RUn gRPC server:

```base
python grpc_server.py
```

###### create data (post request) curl:
```bash
grpcurl -plaintext \
  -d '{ "title": "GRPC new book", "author": "Mbr Sagor", "published_year": 2025 }' \
  localhost:50051 book.BookService/CreateBook
```
