import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTrash } from '@fortawesome/free-solid-svg-icons';

import Person from '../../styles/person.svg'
import './index.css';
import { Button } from 'react-bootstrap';
import { useContext } from 'react';
import { AuthContext } from '../../router/pages/auth/AuthProvider';

export default function UserCard(props) {
  const userData = props.user

  const { user } = useContext(AuthContext)

  const deleteUser = () => {

  }
  
  return (
    <div className='card-custom'>
      <div className='img-spot'>
        <img src={Person} alt="card-content" />
      </div>
      <div className='text-spot'>
        <h4> { userData.login } </h4>
        <h5>
          { (userData.wr >= 0 ? '+' : '') + userData.writer_rating + ' WR ' }
          { (userData.er >= 0 ? '+' : '') + userData.editor_rating + ' ER' }
        </h5>
        <div className='bio'>
          <span>
            Bio: { userData.bio }
          </span>
        </div>
      </div>
      {
        user.isAdmin
        ? <div className='footer'>
            <Button variant='outline-danger' onClick={deleteUser}>
              <FontAwesomeIcon icon={faTrash} />
            </Button>
          </div>
        : <></>
      }
    </div>
  );
}