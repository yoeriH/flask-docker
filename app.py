from app import app, db, api

@app.shell_context_processor:
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
