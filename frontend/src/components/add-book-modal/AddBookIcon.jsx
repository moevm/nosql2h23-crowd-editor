import { faPlus } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useState } from "react";

import AddBookModal from ".";
import './index.css'

export default function AddBookIcon() {
  const [show, setShow] = useState(false);

  return (
    <>
      <FontAwesomeIcon className="add-icon" icon={faPlus} onClick={() => setShow(true)} />
      <AddBookModal show={show} setShow={setShow} />
    </>
  )
}