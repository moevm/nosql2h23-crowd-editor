import { useState } from "react";
import Button from "react-bootstrap/esm/Button";
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

import UserCard from "../../../components/card/UserCard";
import './index.css'

/* fix: req on backend -> setUsers */
  const mock = [
  {
    name: 'User Name',
    wr: 1500,
    er: -500,
    bio: 'Some bio data',
    roles: ['Author', 'Editor']
  },
  {
    name: 'User PlaceHolder',
    wr: 0,
    er: 0,
    bio: 'Some bio data',
    roles: ['Author', 'Editor']
  },
  {
    name: 'User Long Name',
    wr: -1500,
    er: 500,
    bio: 'Some bio data',
    roles: ['Editor']
  },
  {
    name: 'User',
    wr: 150000000,
    er: -500,
    bio: 'Some bio data Some bio data Some bio data Some bio data Some bio data Some bio data 123 Some bio data Some bio data Some bio data Some bio data Some bio data Some bio data Some bio data',
    roles: ['Author']
  },
]

export default function Users() {
  const [users, setUsers] = useState([...mock, ...mock])

  return (
    <div className="users-wrap">
      <InputGroup className="mb-3">
        <Form.Control className="input-custom" placeholder="Search" />
        {/* <Button className="btn-outlined-custom" variant="outlined-primary">
          <FontAwesomeIcon icon="fa-solid fa-magnifying-glass" />
        </Button> */}
      </InputGroup>
      <div className="users-list">
        {
          users.map((user, i) => 
            <UserCard user={user} key={i} />
          )
        }
      </div>
    </div>
  )
}