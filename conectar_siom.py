import pysftp

hostname = '182.160.26.40'
username = 'siom-pe'
password = 'Cu3nt4.,S10mp3'
with pysftp.Connection(hostname, username= username, password=password) as sftp:
    with sftp.cd('public'):             # temporarily chdir to public
        sftp.put('/my/local/filename')  # upload file to public/ on remote
        sftp.get('remote_file')         # get a remote file