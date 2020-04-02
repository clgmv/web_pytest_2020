import pytest

@pytest.fixture(scope='session')
def login1():
    print('这是前置登陆')
    yield
    print('这是后置清除数据')