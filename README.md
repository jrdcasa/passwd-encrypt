# Example Package

This is a simple package to encrypt and decrypt strings using RSA keys.

A possible application can be to encrypt a password when [parakamiko library](http://www.paramiko.org/) is used to make a SSH connection with password. Although is preferable to make a key without password to the SSH connection, sometimes this method does not work, for example if you need to make a connection to **localhost**

As example:

This code is not recommend due to the password is going in plain text
```python
import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='localhost', username='user', password='12345678')
client.exec_command('ls', timeout=5)
```

This code is better:

*  First generate the encrypted password in a file.:

```python
from passwd_encrypt.passwd_encrypt import pw_create_rsa_key, pw_encrypt_msg
# First you generate a couple of RSA keys and then encrypt the password.
pw_create_rsa_key("mykey")
public_key="mykey.pem.pub"
pw_encrypt_msg(public_key, '12345678')
# The password is stored in a cyphered file named "passwd_encrypted.bin"
```

* Now in the code using paramiko to stablish a SSH connection, use the following commands:

```python
import paramiko
from passwd_encrypt.passwd_encrypt import pw_decrypt_msg

# Get the pass_decrypt
private_key="mykey.pem"
pass_decrypt = pw_decrypt_msg(private_key, "passwd_encrypted.bin")

# SSH connection
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='localhost', username='user', password=pass_decrypt)
client.exec_command('ls', timeout=5)
```
The important here is to get the generated private_key in a safe place.
Using this library you can distibute a source code with SSH connection based on passwords without to reveal the password in the code.