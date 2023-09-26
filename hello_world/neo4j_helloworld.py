from neo4j import GraphDatabase
from TOKENS import neoj4_TOKEN

class HelloWorldExample:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def write_node_with_message(self, message):
        with self.driver.session() as session:
            greeting = session.execute_write(self._write_node_with_message, message)
            print(greeting)

    def get_nodes(self):
        with self.driver.session() as session:
            result = session.execute_read(self._get_all_nodes)
            print(result)

    def delete_nodes(self):
        with self.driver.session() as session:
            result = session.execute_write(self._delete_all_nodes)
            print(result)

    @staticmethod
    def _write_node_with_message(tx, message):
        result = tx.run("CREATE (a:Greeting {message: $message}) "
                        "RETURN 'Message: ' + a.message + '; from node ' + id(a)", message=message)
        return result.single()[0]
    
    @staticmethod
    def _get_all_nodes(tx):
        result = tx.run("MATCH (n) RETURN n")
        return list(result)

    @staticmethod
    def _delete_all_nodes(tx):
        result = tx.run("MATCH (n) DELETE n")
        print(result)

    
if __name__ == "__main__":
    greeter = HelloWorldExample("neo4j+s://9bd88fdd.databases.neo4j.io", "neo4j", neoj4_TOKEN)
    print('INFO::Записываем новый узел с сообщением "I am node 1"')
    greeter.write_node_with_message("I am node 1")
    print('INFO::Записываем новый узел с сообщением "I am node 2"')
    greeter.write_node_with_message("I am node 2")
    print('INFO::Выводим информацию обо всех узлах')
    greeter.get_nodes()
    print('INFO::Таким образом, запись в БД работает')
    # greeter.delete_nodes()
    greeter.close()