import { useContext, useState } from "react";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useNavigate } from 'react-router-dom';

import { AuthContext } from "./AuthProvider";

import BigLogo from '../../../styles/big-logo.svg'
import '../../../styles/inputs.css'
import './index.css'


export default function Auth() {
  const { user, login } = useContext(AuthContext);
  const navigate = useNavigate();

  const windowTypes = {
    register: 'register',
    login: 'login'
  }

  const [windowType, setWindow] = useState(windowTypes.login)

  const changeType = () => {
    setWindow(
      windowType === windowTypes.login 
        ? windowTypes.register 
        : windowTypes.login
    )
  }

  const submit = (event) => {
    /* fix: send auth req */
    event.preventDefault();
    const username = event.target.login.value;
    const password = event.target.login.password;
    login({ username });
    navigate('/');
  }

  return (
    <div className="window-wrap">
      <div className="card-window">
        <img src={BigLogo} alt="React Logo" />
        <Form className="d-flex flex-column" onSubmit={submit}>
          <Form.Group className="mb-3">
            <Form.Control
              name="login"
              className="input-custom"
              placeholder="Login"
            />
          </Form.Group>
          <Form.Group className="mb-3">
            <Form.Control 
              name="password"
              className="input-custom" 
              type="password" 
              placeholder="Password" 
            />
          </Form.Group>
          {
            windowTypes[windowType] === windowTypes.register
              ? <Form.Group className="mb-3" controlId="formRepeatPassword">
                  <Form.Control className="input-custom" type="password" placeholder="Repeat password" />
                </Form.Group>
              : <></>
          }
          <div className="d-flex flex-column w-100">
            <Button className="btn-auth btn-custom" variant="primary" type="submit">
              Submit
            </Button>
            <Button className="link-custom" variant="link" onClick={changeType}>
              Or { windowTypes[windowType] }
            </Button>
          </div>
        </Form>
      </div>
    </div>
  );
};
