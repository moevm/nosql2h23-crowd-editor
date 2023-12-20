from neo4j import GraphDatabase
from token import TOKEN, URL


driver = GraphDatabase.driver(URL, auth=("neo4j", TOKEN))

def get_users():
    return "", []


def get_books():
    return "", []


def add_user(user_desc: dict):
    def _check_unique(tx):
        result = tx.run("MATCH (n:User {login: $login}) RETURN (n)",
                        login=user_desc['login'])
        return len(list(result)) == 0
    def _add_user(tx):
        result = tx.run("CREATE (user:User {"
                        "    login: $login,"
                        "    password_hash: $password_hash,"
                        "    bio: $bio,"
                        "    writer_rating: 0,"
                        "    editor_rating: 0,"
                        "    role: $role"
                        "    }) "
                        "RETURN 'Created user with login ' + $login", 
                        login=user_desc['login'],
                        password_hash=user_desc['password_hash'],
                        bio=user_desc['bio'],
                        role=user_desc['role'])
        return result.single()[0]
    # проверяем уникальность логина
    with driver.session() as session:
        try:
            res = session.execute_write(_check_unique)
            if not res:
                return "user with this login already exists!"
        except Exception as e:
            res = f"{type(e).__name__}: {e}"
            return res
    # записываем 
    with driver.session() as session:
        try:
            res = session.execute_write(_add_user)
            res = ""
        except Exception as e:
            res = f"{type(e).__name__}: {e}"
    return res


def add_book(book_desc: dict):
    return ""


def filter_users(filter_desc: dict):
    return ""


def filter_books(filter_desc: dict):
    return ""


def edit_user(user_desc: dict):
    return True


def edit_book(book_desc: dict):
    return True