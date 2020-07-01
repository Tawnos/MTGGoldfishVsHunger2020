from azure.identity import InteractiveBrowserCredential
from azure.keyvault.secrets import SecretClient


authority_host_uri = 'https://login.microsoftonline.com'

tenant = 'a1d447fd-59ac-4bff-8313-5471c9761bd5'
authority_uri = authority_host_uri + '/' + tenant
resource_uri = 'https://management.core.windows.net/'
client_id = '04b07795-8ddb-461a-bbee-02f9e1bf7b46'

credential = InteractiveBrowserCredential(authority_uri=authority_uri, tenant_id=tenant)

secret_client = SecretClient(vault_url="https://vshunger2020.vault.azure.net", credential=credential)
apiKey = secret_client.get_secret("PledgelingAPIKey")
apiKey = secret_client.get_secret("PledgelingPartnerKey")
print(apiKey.value)