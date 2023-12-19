import NavBar from "./navbar";

export default function Main({ children }) {
  return (
    <div>
      <NavBar />
      { children }
    </div>
  );
}