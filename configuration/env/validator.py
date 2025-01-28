import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')

class EnvValidator:
    REQUIRED_ENV_VARS = [
        'SECRET_KEY',
        'PORTA'
    ]

    @staticmethod
    def load_and_validate_env(dotenv_path=dotenv_path):
        """Carrega e valida as variáveis de ambiente."""
        try:
            load_dotenv(dotenv_path)
            env_vars = dict(os.environ)

            # Verificar variáveis obrigatórias
            missing_vars = [var for var in EnvValidator.REQUIRED_ENV_VARS if var not in env_vars]
            if missing_vars:
                raise EnvironmentError(f"As seguintes variáveis de ambiente estão ausentes: {', '.join(missing_vars)}")

            # Validações adicionais (exemplo: conversão para int e validação de faixa)
            env_vars['PORTA'] = int(env_vars['PORTA'])
            if not 1 <= env_vars['PORTA'] <= 65535:
                raise ValueError("A porta deve ser um número inteiro entre 1 e 65535")

            return env_vars
        except Exception as e:
            # Se quiser registrar o erro mesmo sem o logging configurado, pode usar print:
            print(f"Erro ao carregar as variáveis de ambiente: {str(e)}")
            raise

# Chamar a validação e armazenar o resultado
try:
    env_config = EnvValidator.load_and_validate_env()
    # Usar as variáveis de ambiente
    print(f"A porta definida é: {env_config['PORTA']}")
except EnvironmentError as e:
    print(f"Erro: {str(e)}")