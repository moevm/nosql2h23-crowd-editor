import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';

import Logo from '../../styles/logo.svg'
import './index.css'

export default function NavBar() {
  return (
    <Navbar expand="lg" className='navbar'>
      <Container>
        <Navbar.Brand className='header' href="/">
          <img src={Logo} alt='logo' />
          CrowdWriters
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="links me-auto">
            <Nav.Link href="/">Main</Nav.Link>
            <Nav.Link href="books">Books</Nav.Link>
            <Nav.Link href="users">Users</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}