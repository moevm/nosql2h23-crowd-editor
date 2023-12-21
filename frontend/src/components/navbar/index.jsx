import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

import Logo from '../../styles/logo.svg'
import './index.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCircleUser } from '@fortawesome/free-solid-svg-icons'
import AddBookIcon from '../add-book-modal/AddBookIcon';

export default function NavBar() {
  return (
    <Navbar className='navbar'>
      <Container fluid style={{ maxWidth: '1600px' }}>
        <Navbar.Brand className='header' href='/'>
          <img src={Logo} alt='logo' />
          CrowdWriters
        </Navbar.Brand>
        <Navbar.Toggle />
        <Navbar.Collapse>
          <Nav className='links me-auto'>
            <Nav.Link href='/'>Main</Nav.Link>
            <Nav.Link href='books'>Books</Nav.Link>
            <Nav.Link href='users'>Users</Nav.Link>
          </Nav>
          <div className='icon-links'>
            <AddBookIcon />
            <Nav.Link href='profile'>
              <FontAwesomeIcon icon={faCircleUser} />
            </Nav.Link>
          </div>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}