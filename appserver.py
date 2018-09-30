"""
appserver.py
- creates an application instance and runs the server
"""

if __name__ == '__main__':
    from app.application import create_app
    app = create_app()
    app.run()
