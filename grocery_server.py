import grpc
from concurrent import futures
import grocery_pb2_grpc as pb2_grpc
import grocery_pb2 as pb2
from product_finder import ProductFinder


class GroceryService(pb2_grpc.GroceryServicer):

    def __init__(self, *args, **kwargs):
        self.p = ProductFinder()

    def GetProducts(self, request, context):
        search_term = request.search_term
        self.p.search(search_term)

        result = pb2.Results()

        for product in self.p.products.values():
            new_product = result.products.add()
            new_product.name = product.name
            new_product.id = product.id
            new_product.description = product.description
            new_product.image = product.image
            new_product.price = product.price

        return result


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GroceryServicer_to_server(GroceryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
