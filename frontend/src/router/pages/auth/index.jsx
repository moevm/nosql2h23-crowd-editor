import { useContext, useState } from "react";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useNavigate } from 'react-router-dom';

import { AuthContext } from "./AuthProvider";

import BigLogo from '../../../styles/big-logo.svg'
import '../../../styles/inputs.css'
import './index.css'
import AuthAPI from "../../../api/requests/auth";


export default function Auth() {
  const { user, login } = useContext(AuthContext);
  const navigate = useNavigate();

  const windowTypes = {
    register: 'register',
    login: 'login'
  }

  const [windowType, setWindow] = useState(windowTypes.login);
  const [isAuthor, setAuthor] = useState(false);
  const [isEditor, setEditor] = useState(false);

  const changeType = () => {
    setWindow(
      windowType === windowTypes.login 
        ? windowTypes.register 
        : windowTypes.login
    );
  }

  const submit = (event) => {
    /* fix: send auth req */
    event.preventDefault();
    const username = event.target.login.value;
    const password = event.target.password.value;

    const successfully = () => {
      login({ username });
      navigate('/');
    }

    if (windowType === windowTypes.register) {
      const bio = event.target.bio.value;
      AuthAPI.register({
        login: username,
        bio,
        password_hash: password,
        role: 'user'
      })
        .then(successfully)
        .catch((err) => console.log(err))
    } else {
      AuthAPI.login(username, password)
        .then(successfully)
        .catch(err => console.log(err))
    }
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
              ? <div>
                  <Form.Control
                    as="textarea"
                    placeholder="Some words about yourself..."
                    style={{ maxHeight: '100px', resize: 'none' }}
                    name="bio"
                  />
                </div> 
              : <></>
          }
          <div className="d-flex flex-column w-100">
            <Button className="btn-auth btn-custom" variant="primary" type="submit">
              Submit
            </Button>
            <Button className="link-custom" variant="link" onClick={changeType}>
              Or { windowTypes[windowType] === windowTypes.register ? windowTypes.login : windowTypes.register }
            </Button>
          </div>
        </Form>
      </div>
    </div>
  );
};
