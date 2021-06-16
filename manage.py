from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand

app= create_app('development')
# app= create_app('production')
# app= create_app('test')

manager = Manager(app)
manager.add_commad('server',Server)

migrate = Migrate(app,db)
migrate.add_commad('db',MigrateCommand)




if __name__ == '__main__':
    manager.run()