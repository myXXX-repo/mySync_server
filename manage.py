from mySync import create_server
from flask_script import Manager

server = create_server()
manager = Manager(server)

if __name__ == '__main__':
    manager.run()
