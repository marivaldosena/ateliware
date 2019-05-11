import pytest
from flask_script import Manager
from app import create_app

manager = Manager(create_app)


@manager.command
def test(coverage=False):
    comandos = ['-s', './web/app/tests', '-p', 'no:warnings']
    if coverage:
        comandos.append('--cov')

    pytest.main(comandos)


if __name__ == '__main__':
    manager.run()
