import Person from '../../styles/person.svg'

import './index.css';

export default function UserCard(props) {
  const userData = props.user

  return (
    <div className='card-custom'>
      <div className='img-spot'>
        <img src={Person} alt="card-content" />
      </div>
      <div className='text-spot'>
        <h4> { userData.name } </h4>
        <h5>
          { (userData.wr >= 0 ? '+' : '') + userData.wr + ' WR ' }
          { (userData.er >= 0 ? '+' : '') + userData.er + ' ER' }
        </h5>
        <div className='bio'>
          <span>
            Roles: { userData.roles.join(', ') }
          </span>
          <span>
            Bio: { userData.bio }
          </span>
        </div>
      </div>
    </div>
  );
}