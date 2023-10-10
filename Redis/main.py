#First App for connecting to Redis and run some commands
#Care:
#  - sudo systemctl status redis - Show status of server
#  - sudo systemctl stop redis - Stop redis server
#  - sudo redis-server /etc/redis/redis1.conf  - Start or Restart redis server by changed options
#  - redis-cli -p 6380 run client by some parameters

import redis

redis_connection = redis.Redis(host='45.195.250.138', port=6380, db=0)
redis_connection.set('productName', 'New Redis App')
print(redis_connection.get('productName'))