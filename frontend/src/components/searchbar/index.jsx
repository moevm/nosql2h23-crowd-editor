import Button from "react-bootstrap/esm/Button";
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearch } from '@fortawesome/free-solid-svg-icons';
import { useState } from "react";

export default function SearchBar(props) {
  const [search, setSearch] = useState('');

  return (
    <InputGroup className="mb-3">
      <Form.Control 
        className="input-custom"
        placeholder="Search"
        onChange={(e) => setSearch(e.target.value)}
      />
      <Button onClick={() => props.searchCallback(search)} className="btn-outlined-custom" variant="outlined-primary">
        <FontAwesomeIcon icon={faSearch} />
      </Button>
    </InputGroup>
  );
}