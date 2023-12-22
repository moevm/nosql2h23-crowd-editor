import { http } from "..";

export default class BooksAPI {
  static async getAllBooks() {
    return http.get('/books/all');
  }

  static async createBook(params) {
    /**
     * title: string
     * genre: string
     * date?: Date
     * text?: string
     * author_login: string
     */
    return http.post('book/add', params);
  }
}