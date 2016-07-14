from unittest import TestCase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.controller import PostController
from app.models import Post


class TestPostController(TestCase):
    def setUp(self):
        engine = create_engine('mysql://root:password@localhost/unitTest')
        Post.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()

    def test_add_new_data(self):
        postController = PostController(self.session)
        expectedPost = Post("titletest", "bodytest")
        postController.add_new_data("titletest", "bodytest")
        list = self.session.query(Post).filter(Post.title == "titletest").all()
        self.assertEquals(expectedPost,list[0])

    def tearDown(self):
        self.session.query(Post).delete()
        self.session.commit()
