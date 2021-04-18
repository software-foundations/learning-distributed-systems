# -> python
virtualenv -p python3 venv-learning-distributed-systems
source venv-learning-distributed-systems/bin/activate

pip install celery==5.0.5
pip install redis==3.5.3
pip freeze > requirements.txt

# -> redis

# https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04-pt
sudo apt update
sudo apt install redis-server

sudo nano /etc/redis/redis.conf
# 	supervised no
# 	to
# 	supervised systemd

# check
sudo systemctl status redis

# to disbale redis in startup
sudo systemctl disable redis

sudo systemctl restart redis

# command line
redis-cli
ping
# Output: PONG

# creating keys
set test "It's working!"
get test

# go out redis
exit

sudo systemctl restart redis
redis-cli
get test # test if test value is still defined
exit

# linking redis to localhost
sudo nano /etc/redis/redis.conf
# 	locale bind 127.0.0.1 ::1 and uncomment

sudo systemctl restart redis

# install netstat
sudo apt install net-tools

# to check if the alteration is running
sudo netstat -lnp | grep redis

# creating a password for redis
sudo nano /etc/redis/redis.conf
# 	uncomment "# requirepass foobared"
# 	change foobared to a secure password
# 	use the openssl to generate a strong password
openssl rand 60 | openssl base64 -A

sudo systemctl restart redis.service

# login in redis with authentication
redis-cli
auth <my-password>
quit

# renaming dangerous commands
sudo nano  /etc/redis/redis.conf
# . . .
# It is also possible to completely kill a command by renaming it into
# an empty string:
#
# rename-command FLUSHDB ""
# rename-command FLUSHALL ""
# rename-command DEBUG ""
# . . .

sudo systemctl restart redis.service

# linking to git repository
git remote add origin git@github.com:software-foundations/design-patterns.git