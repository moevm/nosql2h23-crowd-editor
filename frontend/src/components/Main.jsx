import Container from "react-bootstrap/esm/Container";
import NavBar from "./navbar";

export default function Main({ children }) {
  return (
    <div>
      <NavBar />
      <Container fluid style={{ maxWidth: '1600px' }}>
        { children }
      </Container>
    </div>
  );
}