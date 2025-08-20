from app import app

if __name__ == "__main__":
    app.run()

'''
# Configurações para WINDOWS
from waitress import serve

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
'''