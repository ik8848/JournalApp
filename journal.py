from app import journal_app, db
from app.models import User, Post

@journal_app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
