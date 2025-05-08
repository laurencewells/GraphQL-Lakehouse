import requests

DATABRICKS_HOST = "<your-databricks-host>"
DATABRICKS_CLIENT_ID = '<your-client-id>'
DATABRICKS_CLIENT_SECRET = '<your-client-secret>'
DATABRICKS_TOKEN_URL = f"{DATABRICKS_HOST}/oidc/v1/token"

def get_access_token():
    response = requests.post(
        DATABRICKS_TOKEN_URL, 
        auth=(DATABRICKS_CLIENT_ID, DATABRICKS_CLIENT_SECRET),
        data={
        "grant_type": "client_credentials",
        "scope": "all-apis"
    })
    response.raise_for_status()
    return response.json()["access_token"]

def call_app():
    bearer = get_access_token()
    response = requests.get(
        f"<your-databricks-app-graph-api>",
        headers={"Authorization": f"Bearer {bearer}"},
        params={
            "query": """{
                    customer(id:412446) {
                        name
                        address
                        nation{
                        name
                        }
                    }
                }"""
        }
    )
    response.raise_for_status()
    print(response.json())

if __name__ == "__main__":
    call_app()