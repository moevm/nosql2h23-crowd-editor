import React, { useContext, useEffect, useState } from 'react';
import { Modal, Button, Form } from 'react-bootstrap';
import BooksAPI from '../../api/requests/books';
import { AuthContext } from '../../router/pages/auth/AuthProvider';

export default function AddBookModal ({ show, setShow }) {
  const [title, setTitle] = useState('');
  const [genre, setGenre] = useState('');

  const { user } = useContext(AuthContext)

  const handleClose = () => setShow(false);

  const handleSubmit = (event) => {
    event.preventDefault();
    BooksAPI.createBook({
      title,
      genre,
      date: (new Date()).toLocaleDateString('en-US'),
      text: '',
      author_login: user.username
    }).catch(err => console.log(err))
    handleClose();
  };

  return (
    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
          <Modal.Title>Add a New Book</Modal.Title>
      </Modal.Header>
      <Modal.Body>
          <Form onSubmit={handleSubmit}>
              <Form.Group controlId="title">
                  <Form.Label>Book Name</Form.Label>
                  <Form.Control 
                    className='input-custom'
                    type="text" 
                    placeholder="Enter book name" 
                    value={title} 
                    onChange={(e) => setTitle(e.target.value)} 
                  />
              </Form.Group>
              <Form.Group controlId="genreSelector">
                  <Form.Label>Genre</Form.Label>
                  <Form.Select
                    className='input-custom'
                    value={genre}
                    onChange={(e) => setGenre(e.target.value)}
                  >
                    <option value="fiction">Fiction</option>
                    <option value="nonfiction">Non-fiction</option>
                    <option value="fantasy">Fantasy</option>
                    <option value="mystery">Mystery</option>
                  </Form.Select>
              </Form.Group>
              <Modal.Footer>
                <Button
                  disabled={!title || !genre}
                  className='btn-outlined-custom'
                  type="submit"
                >
                  Save Changes
                </Button>
              </Modal.Footer>
          </Form>
      </Modal.Body>
    </Modal>
  );
}