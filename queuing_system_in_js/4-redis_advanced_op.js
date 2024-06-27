// this file is used to create a redis client
import redis from 'redis';

const client = redis.createClient();
const ERROR_MESSAGE = 'Redis client not connected to the server';

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const handleHsetResponse = (err, reply) => {
  if (err) {
    console.log(ERROR_MESSAGE, err);
  } else {
    console.log('Reply:', reply);
  }
};

client.hset('HolbertonSchools', 'Portland', '50', handleHsetResponse);
client.hset('HolbertonSchools', 'Seattle', '80', handleHsetResponse);
client.hset('HolbertonSchools', 'New York', '20', handleHsetResponse);
client.hset('HolbertonSchools', 'Bogota', '20', handleHsetResponse);
client.hset('HolbertonSchools', 'Cali', '40', handleHsetResponse);
client.hset('HolbertonSchools', 'Paris', '2', handleHsetResponse);

client.hgetall('HolbertonSchools', (err, reply) => {
  if (err) {
    console.log(ERROR_MESSAGE, err);
  } else {
    console.log(reply);
  }
});
