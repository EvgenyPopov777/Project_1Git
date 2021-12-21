import json
import falcon
from waitress import serve
from  falcon import App, Request, Response,HTTP_201, HTTP_400, HTTP_404
BOOKS ={
    1:"Thomas More.Utopia",
    2:"The Art of War",
    3:"What do women want"
}
class BooksListResourse:
    def on_get(self,req: Request, res: Response):
        books_as_list =[
            {"id":book_id,"name":name_book}
            for book_id, name_book in BOOKS.items()
        ]
        res.text = json.dumps(books_as_list)

    def on_post(self,req:Request, res:Response):
        media: dict = req.get_media()
        data: dict = json.loads(media["data"])
        try:
            book_id = int(data["id"])
            book_name = data["name"]
        except (ValueError,KeyError):
            res.status = falcon.HTTP_400
            result ={"messge": "bad request, fields 'id' (int) and 'name' ()str required"}
        else:
            if book_id in BOOKS:
                res.status = falcon.HTTP_400
                result = {"message": f"book with id #{book_id} already exists"}
            else:
                res.status = falcon.HTTP_201
                result ={"id":book_id, "name": book_name}
        res.media =result
class  BooksDetailsResourse:
    def on_get(self, req:Request, res:Response,book_id:str):
        try:
            book_id = int(book_id)
            name = BOOKS[book_id]
        except ValueError:
            res.status =falcon.HTTP_404
            result ={"message": f"I'm sorry, but such a book has not been found {book_id!r}"}#если вписать буквы
        except KeyError:
            res.status =falcon.HTTP_404
            result ={"message": f"book #{book_id!r} I'm sorry, but such a book has not been found"}# чтобы не вылизала 500 ошибка
        else:
            result ={"id":book_id,"name":name}

            result = {"id":book_id,"name":name}
        res.text = json.dumps(result)
books_list = BooksListResourse()
books_details = BooksDetailsResourse()

app = App()
app.add_route("/books", books_list)
app.add_route("/books/{book_id}",books_details)



serve(app, host='127.0.0.1', port=8041)








# def main():
#     pass
#     # demo_dump_to_json()
# main()


