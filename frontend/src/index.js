import * as React from "react";
import * as ReactDOM from "react-dom/client";

import "./index.css";
import 'bootstrap/dist/css/bootstrap.min.css';

import Router from "./router";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <Router />
  </React.StrictMode>
);