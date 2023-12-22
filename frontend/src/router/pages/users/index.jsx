import { useEffect, useState } from "react";

import UserCard from "../../../components/card/UserCard";
import './index.css'
import UsersAPI from "../../../api/requests/users";
import SearchBar from "../../../components/searchbar";

export default function Users() {
  const [users, setUsers] = useState([])

  useEffect(() => {
    UsersAPI.getAllUsers()
      .then((res) => {
        console.log(res.data)
        if (res.data) {
          setUsers(res.data)
        }
      })
      .catch((err) => console.log(err))
  }, [])

  const searchCallback = (login) => {
    UsersAPI.filterUsers(
      { login }, 
      ['login', 'writer_rating', 'editor_rating', 'bio']
    )
      .then(res => {
        if (res.data) {
          setUsers(res.data);
        }
      })
      .catch(err => console.log(err))
  }

  return (
    <div className="users-wrap">
      {
        users.length 
      ? <div>
          <SearchBar searchCallback={searchCallback} />
          <div className="users-list">
            { users.map((user, i) => <UserCard user={user} key={i} />) }
          </div>
        </div>
        : <h2> Похоже пользователей ещё нет... или у нашего сервера проблемки ^-^ </h2>
      }
    </div>
  )
}