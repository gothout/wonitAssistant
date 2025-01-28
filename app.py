from flask import Flask
from flask_socketio import SocketIO
from werkzeug.routing.exceptions import BuildError
from configuration.rest_err.error_handler import ErrorHandler
from configuration.env.validator import EnvValidator  # Import do validador

# Validação e carregamento das variáveis de ambiente
EnvConfig = EnvValidator.load_and_validate_env()
print(EnvConfig)

app = Flask(__name__,
            template_folder='templates',
            static_folder='templates',
            static_url_path='')

@app.errorhandler(BuildError)
def handle_build_error(error):
    return ErrorHandler.handle_error(error, 500)

# Initialize Socket.IO here
socketio = SocketIO(app)

# Configurar a chave secreta e o socket
app.secret_key = EnvConfig['SECRET_KEY']
socketio.init_app(app)

# Obter a porta do dicionário de configuração
PORTA = EnvConfig['PORTA']

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=int(PORTA), debug=True, allow_unsafe_werkzeug=True)
