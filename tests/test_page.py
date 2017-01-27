from .helpers import TestCase
from app.models import Supervisors


class TestPage(TestCase):
    def test_header(self):
        rv = self.client.get('/')
        assert b'Home' in rv.data

    def test_db(self):
        pass
        # import pdb; pdb.set_trace()
        # self.assertEqual(len(Supervisors.query.all()), 0)
        # s = Supervisors(name='localhost')
        # self.db.add(s)
        # self.assertEqual(len(Supervisors.query.all()), 1)
