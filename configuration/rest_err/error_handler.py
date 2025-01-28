# error_handler.py

from flask import jsonify
from .error_messages import ERROR_MESSAGES

class ErrorHandler:

    @staticmethod
    def handle_error(error, status_code):
        if not error:
            message = ERROR_MESSAGES.get(status_code, "Erro desconhecido.")
            return jsonify({'error': message, 'status_code': status_code}), status_code
        else:
            return jsonify({'error': error, 'status_code': status_code}), status_code