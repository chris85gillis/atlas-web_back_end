// this file is used to create a redis client

import redis from 'redis';

const client = redis.createClient();
const ERROR_MESSAGE = 'Redis client not connected to the server';

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(ERROR_MESSAGE, err);
});
