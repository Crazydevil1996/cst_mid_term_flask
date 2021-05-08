from .books import booksAPI, booksById

def initialize_route(api):
    api.add_resource(booksAPI,'/books')
    api.add_resource(booksById,'/books/<id>')