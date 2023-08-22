from flask import Flask, redirect, url_for
from app.domain.book import Book, db

# db.init_app(app)

class SQLiteStorage:
    def __init__(self):
        self.storage = self.storage

    def add(self,books):
        book = Book()
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("user_detail", id=book.id))
        return render_template(book=book)

    def get(self):
        return self.books

    def delete(self, id):
        del self.books[int(id)]