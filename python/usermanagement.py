import subprocess

def create_user(username, password):
    subprocess.run(['adduser', '--disabled-password', '--gecos', '""', username])
    subprocess.run(['bash', '-c', f"echo {username}:{password} | chpasswd"])

def reset_password(username, new_password):
    subprocess.run(['bash', '-c', f"echo {username}:{new_password} | chpasswd"])

def grant_access(username, directory):
    subprocess.run(['chown', '-R', username, directory])

def set_permission(permission, file):
    subprocess.run(['chmod', '-R', permission, file])

def revoke_access(username, directory):
    subprocess.run(['chown', '-R', 'root', directory])

# Example usage
#create_user('gholi', 'password123')
#reset_password('gholi', 'new456')
grant_access('gholi', '/home/tmpdir/')
set_permission('u+r-w+x,g-r+w-x,o+r-w-x', '/home/tmpdir/')
#revoke_access('gholi', '/home/tmpdir/')
