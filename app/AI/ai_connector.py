import os
import logging
from dotenv import load_dotenv
from app.core.settings import  settings
from infisical_sdk import InfisicalSDKClient
from app.core.exceptions import SecretManagerException

logger =logging.getLogger(__name__)
class SecretManager:
        @staticmethod
        def get_secret_key()->str:
                try:
                        load_dotenv()
                        client = InfisicalSDKClient(host = settings.INFISICAL_URL)
                        client.auth.universal_auth.login(
                                client_id=os.getenv("CLIENT_ID"),
                                client_secret =os.getenv("CLIENT_SECRET")
                                )
                        secretkey = client.secrets.get_secret_by_name(
                                secret_name="GROQ_API_KEY",
                                environment_slug=settings.ENVIRONMENT,
                                project_id=os.getenv("project_id"),
                                secret_path="/"
                        )
                        logger.info("Groq API key retrieved successfully")
                        return secretkey.secretValue
                except Exception as e:
                        logging.exception("Infisical secret retrieval failed")
                        raise SecretManagerException(detail="Failed to retrieve secrets")
