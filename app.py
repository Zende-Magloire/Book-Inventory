from flask import Flask, request, render_template
import sqlite3

db = sqlite3.connect('books.db', check_same_thread=False)
db.row_factory = sqlite3.Row
cursor = db.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    cursor.execute("SELECT books.book_id, books.title, authors.name AS author_name, genres.name AS genre_name, books.publication_year, books.is_read, books.isbn, books.rating FROM books JOIN authors ON books.author_id = authors.author_id JOIN genres ON books.genre_id = genres.genre_id")
    books = cursor.fetchall()
    for book in books:
        book_id, title, author_name, genre_name, publication_year, is_read, isbn, rating = book
        #print(f"Book ID: {book_id}, Title: {title}, Author: {author_name}, Genre: {genre_name}")

    cursor.execute("SELECT * FROM authors")
    authors = cursor.fetchall()
    cursor.execute("SELECT * FROM genres")
    genres = cursor.fetchall()
    cursor.execute("SELECT * FROM book_loans")
    book_loans = cursor.fetchall()

    return render_template('home.html', title="Book collection", books=books)


if __name__ == '__main__':
    app.run(debug=True, port=61983, host = '0.0.0.0')

