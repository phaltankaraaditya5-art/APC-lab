from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self):
        print("Uploading file to Google Drive")

    def download_file(self):
        print("Downloading file from Google Drive")

    def delete_file(self):
        print("Deleting file from Google Drive")


class Dropbox(CloudStorage):
    def upload_file(self):
        print("Uploading file to Dropbox")

    def download_file(self):
        print("Downloading file from Dropbox")

    def delete_file(self):
        print("Deleting file from Dropbox")


services = [GoogleDrive(), Dropbox()]

for service in services:
    service.upload_file()
    service.download_file()
    service.delete_file()