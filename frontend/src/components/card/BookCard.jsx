import Book from '../../styles/book.svg'

import './index.css';

export default function BookCard(props) {
  return (
    <div className='card-custom'>
      <div className='img-spot'>
        <img src={Book} alt="card-content" />
      </div>
      <div className='text-spot'>
        <h4> { props.title } </h4>
        <div className='bio'>
          <span>
            { props.description }
          </span>
        </div>
      </div>
    </div>
  );
}