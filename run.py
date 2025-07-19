import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    host = '0.0.0.0' if os.environ.get("PORT") else '127.0.0.1'
    app.run(host=host, port=port)
