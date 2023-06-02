
import config

from ftplib import FTP

# connect to the FTP server
ftp = FTP(config.ftp_server)
ftp.login(config.ftp_username, config.ftp_password)

# Change to the desired remote directory
ftp.cwd('public_html')

# Open the local file in binary mode for uploading
with open('index.html', 'rb') as file:
    # Upload the file to the FTP server
    ftp.storbinary(f'STOR index.html', file)
