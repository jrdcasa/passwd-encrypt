#!/bin/bash
WK=`pwd`
cd $WK

EXEPY="../passwd_encrypt/passwd_encrypt.py"

# Generate the help
echo "*******************************************"
echo "1. Visualize the help."
python $EXEPY -u

echo "*******************************************"
echo "2. Generate the keys."
python $EXEPY -c mykey
echo "*** The files mykey.pem (private) mykey.pem.pub (public) keys have been generated."

echo "*******************************************"
echo "2. Encrypt message."
python $EXEPY -e mykey.pem.pub "Message in a bottle!!!!!"
echo "*** The file passwd_encrypted.bin has been generated."

echo "*******************************************"
echo "3. Decrypt message."
msg="Message in a bottle!!!!!"
python $EXEPY -d mykey.pem passwd_encrypted.bin
echo "*** Message decrypted."
echo "*******************************************"
