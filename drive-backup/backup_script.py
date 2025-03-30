from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os


SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_KEY")
SCOPES = ['https://www.googleapis.com/auth/drive']

def authentication():
    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return credentials


def upload_files(file_path, folder_id=None):
    credentials = authentication()
    service = build('drive', 'v3', credentials=credentials)
    file_metadata = {'name': os.path.basename(file_path)}
    if folder_id:
        file_metadata['parents'] = [folder_id]
    
    media = MediaFileUpload(file_path)
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    
    return file.get('id')
    


def upload_directory(directory_path, parent_folder_id=None):
    credentials = authentication()
    service = build('drive', 'v3', credentials=credentials)
    dir_name = os.path.basename(directory_path)

    folder_metadata = {
        'name': dir_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    
    if parent_folder_id:
        folder_metadata['parents'] = [parent_folder_id]
    
    folder = service.files().create(
        body=folder_metadata,
        fields='id'
    ).execute()
    
    folder_id = folder.get('id')
    
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        
        if os.path.isfile(item_path):
            upload_files(item_path, folder_id)
        elif os.path.isdir(item_path):
            upload_directory(item_path, folder_id)
    
    return folder_id



if __name__ == "__main__":
    upload_directory(os.getcwd(), 'folder_id') # should come from https://drive.google.com/drive/folders/folder_id