PI_IP=192.168.2.36
PI_USER=pi
SERVER_USER=doug
eval 'ssh-agent -s'
ssh-add ~$SERVER_USER/.ssh/id_rsa
while inotifywait -r -e modify,create,delete .
do
	rsync -v -e "ssh -i ~$SERVER_USER/.ssh/id_rsa.pub" $PI_USER@$PI_IP:/var/www/html/ ./html/
    rsync -v -e "ssh -i ~$SERVER_USER/.ssh/id_rsa.pub" $PI_USER@$PI_IP:/usr/lib/cgi-bin ./cgi-bin/
    rsync -v -e "ssh -i ~$SERVER_USER/.ssh/id_rsa.pub" $PI_USER@$PI_IP:/SMARS/ ./SMARS/
done