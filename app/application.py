
def create_app():
    """Creates a Flask app instance"""
    from app.api import app
    app.config.from_object('app.config.BaseConfig')
    return app