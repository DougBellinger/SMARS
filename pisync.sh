PI_IP=192.168.2.36
PI_USER=pi
SERVER_USER=doug
eval 'ssh-agent -s'
ssh-add /home/$SERVER_USER/.ssh/id_rsa
while inotifywait -r -e modify,create,delete .
do
	rsync -r -v -e "ssh -i ~$SERVER_USER/.ssh/id_rsa.pub" ./html/ $PI_USER@$PI_IP:/var/www/html/ 
    rsync -r -v -e "ssh -i ~$SERVER_USER/.ssh/id_rsa.pub" ./cgi-bin/ $PI_USER@$PI_IP:/usr/lib/cgi-bin/ 
    rsync -r -v -e "ssh -i ~$SERVER_USER/.ssh/id_rsa.pub" ./SMARS/ $PI_USER@$PI_IP:/home/$PI_USER/SMARS/
done