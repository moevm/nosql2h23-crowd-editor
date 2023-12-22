import axios from "axios";

const url = 'http://127.0.0.1'
const port = 8080
const baseURL = `${url}:${port}/`

export const http = axios.create({ baseURL })