import requests

class SharePointClient:
    def __init__(self, client_id, client_secret, tenant_id, site_domain, site_name, drive_name='Documents'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.site_domain = site_domain
        self.site_name = site_name
        self.drive_name = drive_name
        self.access_token = self._get_access_token()
        self.site_id = self._get_site_id()
        self.drive_id = self._get_drive_id()

    def _get_access_token(self):
        print('_get_access_token: start')
        # Implements OAuth2 client credentials flow without msal
        token_url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": "https://graph.microsoft.com/.default",
            "grant_type": "client_credentials"
        }
        response = requests.post(token_url, data=data)
        response.raise_for_status()
        return response.json()["access_token"]

    def _get_site_id(self):
        print('_get_site_id: start')
        site_url = f"https://graph.microsoft.com/v1.0/sites/{self.site_domain}/:/sites/{self.site_name}" # 
        response = requests.get(site_url, headers={"Authorization": f"Bearer {self.access_token}"})
        # print(f"Response from _get_site_id: {response.status_code} - {response.text}")
        response.raise_for_status()
        return response.json()['id']

    def _get_drive_id(self):
        print('_get_drive_id: start')
        drive_url = f"https://graph.microsoft.com/v1.0/sites/{self.site_id}/drives"
        response = requests.get(drive_url, headers={"Authorization": f"Bearer {self.access_token}"})
        response.raise_for_status()
        drives = response.json()['value']
        return next(drive['id'] for drive in drives if drive['name'] == self.drive_name)

    def list_files(self):
        print('list_files: start')

        files_url = f"https://graph.microsoft.com/v1.0/drives/{self.drive_id}/root/children"
        response = requests.get(files_url, headers={"Authorization": f"Bearer {self.access_token}"})
        response.raise_for_status()
        files = response.json()['value']
        for file in files:
            print(f">> {file['name']} - {file['webUrl']}")
        return files

    def upload_file(self, local_path, upload_name):
        upload_url = f"https://graph.microsoft.com/v1.0/drives/{self.drive_id}/root:/{upload_name}:/content"
        with open(local_path, 'rb') as file_stream:
            response = requests.put(
                upload_url,
                headers={
                    "Authorization": f"Bearer {self.access_token}",
                    "Content-Type": "application/octet-stream"
                },
                data=file_stream
            )
        if response.status_code in (200, 201):
            print(f"File uploaded successfully: {response.json()['webUrl']}")
        else:
            print(f"Failed to upload file: {response.status_code} - {response.text}")


# ===================================== main =====================================
# To get your tenant ID access this site:
# https://entra.microsoft.com/

# Example usage:
# sp_client = SharePointClient(
#     client_id='YOUR_CLIENT_ID',
#     client_secret='YOUR_CLIENT_SECRET',
#     tenant_id='YOUR_TENANT_ID',
#     site_domain='YOUR_SHAREPOINT_DOMAIN',
#     site_name='YOUR_SHAREPOINT_SITE_NAME'
# )
# sp_client.list_files()
# sp_client.upload_file('/path/to/local/file.txt', 'uploaded_file.txt')

sp_client = SharePointClient(
    client_id='a1b...a1',
    client_secret='5nk...aYG',
    tenant_id='e2d...73',
    site_domain='7_____.sharepoint.com',
    site_name='SFG-MSP'
)
sp_client.list_files()
sp_client.upload_file('/tmp/README_2.pdf', 'README_2.pdf')