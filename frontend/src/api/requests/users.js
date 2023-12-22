import { http } from "..";

export default class UsersAPI {
  static async getAllUsers() {
    return http.get('/users/all');
  }
  static async filterUsers(filter, get) {
    /**
     * filter: {
     *  login: string
     *  password: string
     * }
     * get: [fields to get]
    */
   http.get('/user', { params: { filter: JSON.stringify(filter), get: JSON.stringify(get) } })
  }
}