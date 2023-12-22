from neo4j import GraphDatabase
from token import TOKEN, URL


driver = GraphDatabase.driver(URL, auth=("neo4j", TOKEN))

def transform_dict_to_str_with_brackets(d):
    return '{' + ", ".join(f"{param_name}: " + (f"'{param_value}'" if type(param_value) == str else f"{param_value}") for param_name, param_value in d.items()) + '}'
    

def get_users():
    def _get_users(tx):
        result = tx.run("MATCH (user:User)"
                        "RETURN (user)")
        return [x.data()['user'] for x in result]
    with driver.session() as session:
        try:
            res = session.execute_read(_get_users)
            msg = ""
        except Exception as e:
            msg, res = f"{type(e).__name__}: {e}", []
    return msg, res


def get_books():
    def _get_books(tx):
        result = tx.run("MATCH (book:Book)"
                        "RETURN (book)")
        return [x.data() for x in result]
    with driver.session() as session:
        try:
            res = session.execute_read(_get_books)
            msg = ""
        except Exception as e:
            msg, res = f"{type(e).__name__}: {e}", []
    return msg, res


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
    def _add_book(tx):
        result = tx.run("MATCH (user:User {login: $author_login})"
                        "CREATE (book:Book {"
                        "    title: $title,"
                        "    genre: $genre,"
                        "    date: $date,"
                        "    text: $text"
                        "    })<-[:WROTE]-(user) "
                        "SET book.id=ID(book)"
                        "RETURN 'Created book with title ' + book.title", 
                        title=book_desc['title'],
                        genre=book_desc['genre'],
                        author_login=book_desc['author_login'],
                        date=book_desc['date'],
                        text=book_desc['text'])
        return result.single()[0]
    with driver.session() as session:
        try:
            res = session.execute_write(_add_book)
            res = ""
        except Exception as e:
            res = f"{type(e).__name__}: {e}"
    return res

def filter_users(filter_desc: dict):
    filter_data = filter_desc["filter"]
    get_data = filter_desc['get']
    def _filter_users(tx):
        filter_str = transform_dict_to_str_with_brackets(filter_data)
        result = tx.run(f"MATCH (user:User {filter_str})"
                        f"RETURN (user)")
        return [x.data()['user'] for x in result]
    with driver.session() as session:
        try:
            res = session.execute_read(_filter_users)
            filtered_res = []
            for node in res:
                filtered_res.append(dict((k, v) for k,v in node.items() if k in get_data))
            res = filtered_res
            msg = ""
        except Exception as e:
            msg = f"{type(e).__name__}: {e}"
            res = []
    return msg, res


def filter_books(filter_desc: dict):
    filter_data = filter_desc["filter"]
    get_data = filter_desc['get']
    def _filter_books(tx):
        filter_str = transform_dict_to_str_with_brackets(filter_data)
        result = tx.run(f"MATCH (book:Book {filter_str})"
                        f"RETURN (book)")
        return [x.data()['book'] for x in result]
    with driver.session() as session:
        try:
            res = session.execute_read(_filter_books)
            filtered_res = []
            for node in res:
                filtered_res.append(dict((k, v) for k,v in node.items() if k in get_data))
            res = filtered_res
            msg = ""
        except Exception as e:
            msg = f"{type(e).__name__}: {e}"
            res = []
    return msg, res


def edit_user(update_user_desc: dict):
    filter_data = update_user_desc["filter"]
    set_data = update_user_desc["set"]
    def _edit_user(tx):
        filter_str = transform_dict_to_str_with_brackets(filter_data)
        set_str = ", ".join(f"user.{param_name} = " + (f"'{param_value}'" if type(param_value) == str else f"{param_value}") for param_name, param_value in set_data.items())
        result = tx.run(f"MATCH (user:User {filter_str})"
                        f"SET {set_str}")
    with driver.session() as session:
        try:
            session.execute_write(_edit_user)
            msg = ""
        except Exception as e:
            msg = f"{type(e).__name__}: {e}"
    return msg    


def edit_book(update_book_desc: dict):
    filter_data = update_book_desc["filter"]
    set_data = update_book_desc["set"]
    def _edit_book(tx):
        filter_str = transform_dict_to_str_with_brackets(filter_data)
        set_str = ", ".join(f"book.{param_name} = " + (f"'{param_value}'" if type(param_value) == str else f"{param_value}") for param_name, param_value in set_data.items())
        result = tx.run(f"MATCH (book:Book {filter_str})"
                        f"SET {set_str}")
    with driver.session() as session:
        try:
            session.execute_write(_edit_book)
            msg = ""
        except Exception as e:
            msg = f"{type(e).__name__}: {e}"
    return msg    

def add_book_review(review_info):
    user_login = review_info['user_login']
    book_id = review_info['book_id']
    review_data = review_info['review_data']
    def _add_book_review(tx):
        review_data_str = transform_dict_to_str_with_brackets(review_data)
        result = tx.run("MATCH (user:User {login: $user_login}), (book:Book {id: $book_id})"
                        f"CREATE (user)-[r:REVIEWED {review_data_str}]->(book)"
                        "SET r.id=ID(r)",
                        user_login=user_login, book_id=book_id)
    with driver.session() as session:
        try:
            session.execute_write(_add_book_review)
            msg = ""
        except Exception as e:
            msg = f"{type(e).__name__}: {e}"
    return msg    


def add_critique(critique_info):
    user_src_login = critique_info['user_src_login']
    user_login = critique_info['user_login']
    critique_data = critique_info['critique_data']
    def _add_critique(tx):
        critique_data_str = transform_dict_to_str_with_brackets(critique_data)
        result = tx.run("MATCH (user_src:User {login: $user_src_login}), (user:User {login: $user_login})"
                        f"CREATE (user_src)-[r:CRITIQUED {critique_data_str}]->(user)"
                        "SET r.id=ID(r)",
                        user_src_login=user_src_login,
                        user_login=user_login)
    with driver.session() as session:
        try:
            session.execute_write(_add_critique)
            msg = ""
        except Exception as e:
            msg = f"{type(e).__name__}: {e}"
    return msg    


def add_proposition(proposition_info):
    user_login = proposition_info['user_login']
    book_id = proposition_info['book_id']
    proposition_data = proposition_info['proposition_info']
    def _add_proposition(tx):
        proposition_data_str = transform_dict_to_str_with_brackets(proposition_data)
        result = tx.run("MATCH (user:User {login: $user_login}), (book:Book {id: $book_id})"
                        f"CREATE (user)-[r:PROPOSED {proposition_data_str}]->(book)"
                        "SET r.id=ID(r)",
                        user_login=user_login,
                        book_id=book_id)
    with driver.session() as session:
        try:
            session.execute_write(_add_proposition)
            msg = ""
        except Exception as e:
            msg = f"{type(e).__name__}: {e}"
    return msg   

def filter_wrote_relation(wrote_info):
    user_filter = wrote_info["user_filter"]
    book_filter = wrote_info["book_filter"]
    get = wrote_info["get"] # user, book или r
    def _get_book_author(tx):
        user_filter_str = transform_dict_to_str_with_brackets(user_filter)
        book_filter_str = transform_dict_to_str_with_brackets(book_filter)
        result = tx.run(f"MATCH (user:User {user_filter_str})-[r:WROTE]->(book:Book {book_filter_str})"
                        f"RETURN ({get})")
        return [x.data()[get] for x in result]
    with driver.session() as session:
        try:
            res = session.execute_read(_get_book_author)
            msg = ""
        except Exception as e:
            msg, res = f"{type(e).__name__}: {e}", []
    return msg, res
