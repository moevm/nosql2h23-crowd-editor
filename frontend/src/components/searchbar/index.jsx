import Button from "react-bootstrap/esm/Button";
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

export default function SearchBar() {
  return (
    <InputGroup className="mb-3">
      <Form.Control className="input-custom" placeholder="Search" />
      {/* <Button className="btn-outlined-custom" variant="outlined-primary">
        <FontAwesomeIcon icon="fa-solid fa-magnifying-glass" />
      </Button> */}
    </InputGroup>
  );
}