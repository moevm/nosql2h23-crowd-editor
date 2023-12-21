import Book from '../../styles/book.svg'

import './index.css';

export default function BookCard(props) {
  const bookData = props.book

  return (
    <div className='card-custom'>
      <div className='img-spot'>
        <img src={Book} alt="card-content" />
      </div>
      <div className='text-spot'>
        <h4> { bookData.title } </h4>
        <div className='bio'>
          <span>
            { bookData.description }
          </span>
        </div>
      </div>
    </div>
  );
}