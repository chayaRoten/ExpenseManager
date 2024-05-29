import asyncio
from bson import ObjectId
from app.services import user_CRUD as userFunc
from app.models.user import User
import unittest


class TestHH(unittest.TestCase):

    def test_signUp(self):
        user = User(id=11111, name="aaa", password="s@sw.fdfg")
        result = asyncio.run(userFunc.sign_up(user))
        assert result == "sign up!"
    def test_login(self):
        user = User(id=11111, name="aaa", password="s@sw.fdfg")
        result = asyncio.run(userFunc.login(user))
        assert result == {'_id': ObjectId('663a60044fc5862f937b8e4a'), 'id': 11111, 'name': 'aaa', 'password': 's@sw.fdfg'}



    def test_updateUser(self):
        user = User(id=11111, name="a", password="s@sw.fdfg")
        result = asyncio.run(userFunc.update_user(user))
        assert result == "update user!"



if __name__ == '__main__':
    unittest.main()
