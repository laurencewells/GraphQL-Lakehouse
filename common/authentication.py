import os
from datetime import datetime
from databricks import sql
from databricks.sdk.core import Config, oauth_service_principal
import logging

class DatabricksAuthentication:

    def __init__(self,bearer: str= None) -> None:
        self.server = os.getenv("DATABRICKS_HOST")
        self.path = os.getenv("DATABRICKS_WAREHOUSE_PATH")
        self.bearer = bearer
        self.client = self._get_client()

    def _get_client(self):
        if self.bearer:
            logging.log(logging.INFO, "Using bearer authentication")
            return sql.connect(
                server_hostname=self.server,
                http_path=self.path,
                access_token=self.bearer,
                session_configuration= {"timezone": self._local_tz()},
            )
        local_tz = self._local_tz()
        if "DATABRICKS_TOKEN" in os.environ:
            logging.log(logging.INFO, "Using token authentication")
            return sql.connect(
                server_hostname=self.server,
                http_path=self.path,
                access_token=os.getenv("DATABRICKS_TOKEN"),
                session_configuration= {"timezone": local_tz},
            )
        elif "DATABRICKS_CLIENT_ID" in os.environ:
            logging.log(logging.INFO, "Using machine authentication")
            return sql.connect(
                server_hostname=self.server,
                http_path=self.path,
                credentials_provider=self.__credential_provider,
                session_configuration={"timezone": local_tz},
            )
        else:
            raise ValueError("No authentication method provided")

    def __credential_provider(self):
        config = Config(
            host=f"https://{self.server}",
            client_id=os.getenv("DATABRICKS_CLIENT_ID"),
            client_secret=os.getenv("DATABRICKS_CLIENT_SECRET"),
        )
        return oauth_service_principal(config)

    def _local_tz(self):
        now = datetime.now().astimezone()
        # Get the UTC offset in hours and minutes
        utc_offset = now.strftime('%z')
        # Format the UTC offset as +HH:MM or -HH:MM
        formatted_offset = f"{utc_offset[:3]}:{utc_offset[3:]}"
        return formatted_offset
