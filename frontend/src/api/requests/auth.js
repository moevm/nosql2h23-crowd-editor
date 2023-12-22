import { http } from "..";
import UsersAPI from "./users";

export default class AuthAPI {
  static async register(params) {
    /**
     * login: string
     * bio: string
     * password_hash?: string
     * role: string
    */
    return http.post('user/add', params)
  }

  static async login(login, password_hash) {
    return await UsersAPI.filterUsers({ login, password_hash }, ['login'])
  }
}