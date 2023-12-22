import { useEffect, useState } from "react";

import SearchBar from "../../../components/searchbar";
import BookCard from "../../../components/card/BookCard";
import './index.css'
import BooksAPI from "../../../api/requests/books";

export default function Library() {
  const [books, setBooks] = useState([])

  useEffect(() => {
    BooksAPI.getAllBooks()
      .then((res) => {
        if (res.data) {
          setBooks(res.data)
        }
      })
      .catch((err) => console.log(err))
  }, [])

  return (
    <div className="users-wrap">
      {
        books.length 
      ? <div>
          <SearchBar />
          <div className="users-list">
            { books.map((book, i) => <BookCard book={book.book} key={i} />) }
          </div>
        </div>
        : <h2> Похоже книг ещё нет... или у нашего сервера проблемки ^-^ </h2>
      }
    </div>
  )
}