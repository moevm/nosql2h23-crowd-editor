import { http } from "..";

export default class UsersAPI {
  static async getAllUsers() {
    return http.get('/users/all');
  }
  static async filterUsers(filter, get) {
    /**
     * filter: {
     *  [key]: [value]
     * }
     * get: [fields to get]
    */
   return http.get('/user', { params: { filter: JSON.stringify(filter), get: JSON.stringify(get) } })
  }
}