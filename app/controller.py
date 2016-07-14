from app.models import Post


class PostController():
    def __init__(self, db_session):
        self.db_session = db_session

    def get_all_data(self):
        return Post.query.all()

    def add_new_data(self, title, body):
        post = Post(title, body)
        self.db_session.add(post)
        self.db_session.commit()

    def get_data_by_id(self,id):
        return Post.query.get(id)

    def edit_data_by_id(self,id,title,body):
        post = self.get_data_by_id(id)
        post.title = title
        post.body = body
        self.db_session.commit()

    def delete_data_by_id(self, id):
        post = Post.query.get(id)
        self.db_session.delete(post)
        self.db_session.commit()
