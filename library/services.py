import grpc
from library.models import Book
import book_pb2, book_pb2_grpc

class BookService(book_pb2_grpc.BookServiceServicer):

    def CreateBook(self, request, context):
        book = Book.objects.create(
            title=request.title,
            author=request.author,
            published_year=request.published_year
        )
        return book_pb2.BookResponse(
            id=book.id,
            title=book.title,
            author=book.author,
            published_year=book.published_year
        )

    def GetBook(self, request, context):
        try:
            book = Book.objects.get(pk=request.id)
            return book_pb2.BookResponse(
                id=book.id,
                title=book.title,
                author=book.author,
                published_year=book.published_year
            )
        except Book.DoesNotExist:
            context.abort(grpc.StatusCode.NOT_FOUND, "Book not found")

    def UpdateBook(self, request, context):
        try:
            book = Book.objects.get(pk=request.id)
            book.title = request.title
            book.author = request.author
            book.published_year = request.published_year
            book.save()
            return book_pb2.BookResponse(
                id=book.id,
                title=book.title,
                author=book.author,
                published_year=book.published_year
            )
        except Book.DoesNotExist:
            context.abort(grpc.StatusCode.NOT_FOUND, "Book not found")

    def DeleteBook(self, request, context):
        try:
            book = Book.objects.get(pk=request.id)
            book.delete()
            return book_pb2.BookDeleteResponse(message="Book deleted")
        except Book.DoesNotExist:
            context.abort(grpc.StatusCode.NOT_FOUND, "Book not found")
