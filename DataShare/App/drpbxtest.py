
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
def __datetime(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

access_token = 'ttVqa5_XPaAAAAAAAAAAylEHHmcckHbfcG041udS0MqkXhFnA06ME-RbmjjmO_ul'
transferData = TransferData(access_token)
name="1.txt"
file_from = name
file_to = '/test_dropbox/'+name  # The full path to upload the file to, including the file name

# API v2
transferData.upload_file(file_from, file_to)


access_token = 'ttVqa5_XPaAAAAAAAAAAylEHHmcckHbfcG041udS0MqkXhFnA06ME-RbmjjmO_ul'
dbx = dropbox.Dropbox(access_token)
metadata, f = dbx.files_download('/test_dropbox/'+name)
con=f.content
print(con)
