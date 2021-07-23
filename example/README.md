# Example
``Linux``: You can try **passwd_encrypt** by running **run_test.sh** bash script.

``Windows 10``: TODO

``Command line``:

1. Activate the python enviroment:
 	``source env/bin/activate``
 2. Install the script and its dependences
 	``python setup.py install``
 3. Run the the program from the CLI
 	``python passwd_encrypt.py -c mykey``
	``python passwd_encrypt.py -e mykey.pem "Message"``
 	``python passwd_encrypt.py -d mykey.pem.pub "passwd_encrypted.bin"``
