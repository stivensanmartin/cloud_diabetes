from azureml.core.authentication import InteractiveLoginAuthentication
from azureml.core import Workspace

interactive_auth = InteractiveLoginAuthentication(tenant_id="99e1e721-7184-498e-8aff-b2ad4e53c1c2")
ws = Workspace.get(name='mlw-cloud-udea',
            subscription_id='99b44d16-3153-43c2-b50d-9734378f7aa8',
            resource_group='rg-cloud-udea',
            location='eastus',
            auth=interactive_auth
            )
ws.write_config(path='.azureml')