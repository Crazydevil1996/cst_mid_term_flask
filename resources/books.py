from flask import Response, request
from database.models import books
from flask_restful import Resource

class booksAPI(Resource):
    def get(self):
        book = books.objects().to_json()
        return Response(book, mimetype="application/json", status=200)
    
    def post(self):
        body = request.get_json()
        book = books(**body).save()
        b_id =  book.b_id
        return {'Success' : body}, 200
    
class booksById(Resource):
    def get(self, id):
        book = books.objects.get(b_id= id).to_json()
        return Response(book, mimetype="application/json", status=200)
    
    def put(self, id):
        body = request.get_json()
        books.objects.get(b_id=id).update(**body)
        return {'Book data updated Successfull!!': body}

    def delete(self, id):
        book = books.objects.get(b_id=id).delete()
        return ('Book deleted successfully')
