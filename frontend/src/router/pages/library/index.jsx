import { useState } from "react";

import SearchBar from "../../../components/searchbar";
import BookCard from "../../../components/card/BookCard";
import './index.css'

/* fix: req on backend -> setUsers */
  const mock = [
  {
    title: 'Book title',
    description: 'Some description',
  },
  {
    title: 'Title Placeholder',
    description: 'Some very long long long long long  description',
  },
  {
    title: 'Fake Name',
    description: 'Some fake description',
  },
  {
    title: '404',
    description: 'Bad request. (joke)',
  },
]

export default function Library() {
  const [books, setBooks] = useState([...mock, ...mock])

  return (
    <div className="users-wrap">
      <SearchBar />
      <div className="users-list">
        {
          books.map((book, i) => 
            <BookCard book={book} key={i} />
          )
        }
      </div>
    </div>
  )
}