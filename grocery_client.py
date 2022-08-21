import grpc
import grocery_pb2_grpc as pb2_grpc
import grocery_pb2 as pb2


class GroceryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.GroceryStub(self.channel)

    def get_url(self, search_term):
        """
        Client function to call the rpc for GetServerResponse
        """
        query = pb2.Query(search_term=search_term)
        return self.stub.GetProducts(query)


if __name__ == '__main__':
    client = GroceryClient()
    result = client.get_url('beef')
    print(f'{result}')
