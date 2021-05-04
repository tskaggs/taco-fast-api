from neo4j import GraphDatabase

def connect():
    return GraphDatabase.driver(uri, auth=(user, password))


# def close():
#     self.driver.close()


# def print_greeting(message):
#     with self.driver.session() as session:
#         greeting = session.write_transaction(self._create_and_return_greeting, message)
#         print(greeting)


# @staticmethod
# def _create_and_return_greeting(tx, message):
#     result = tx.run("CREATE (a:Greeting) "
#                     "SET a.message = $message "
#                     "RETURN a.message + ', from node ' + id(a)", message=message)
#     return result.single()[0]


def turd():
    return "Farts!"


class HelloWorldExampleNeo4j:
    pass
