import React, { useState } from 'react';
import { Modal, Button, Form } from 'react-bootstrap';

export default function AddBookModal ({ show, setShow }) {
  const [bookName, setBookName] = useState('');
  const [genre, setGenre] = useState('');

  const handleClose = () => setShow(false);
  const handleSubmit = (event) => {
      event.preventDefault();
      console.log(bookName, genre);
      handleClose();
  };

  return (
    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
          <Modal.Title>Add a New Book</Modal.Title>
      </Modal.Header>
      <Modal.Body>
          <Form onSubmit={handleSubmit}>
              <Form.Group controlId="bookName">
                  <Form.Label>Book Name</Form.Label>
                  <Form.Control 
                      className='input-custom'
                      type="text" 
                      placeholder="Enter book name" 
                      value={bookName} 
                      onChange={(e) => setBookName(e.target.value)} 
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
                  disabled={!bookName || !genre}
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