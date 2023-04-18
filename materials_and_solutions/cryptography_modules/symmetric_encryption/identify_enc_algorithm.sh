while read cipher;
do
    echo '-------------'
    echo $cipher
    openssl enc -d -a $cipher -in message.enc -kfile pwd.pass -pbkdf2
    echo '/n'
done;