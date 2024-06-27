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


const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, value) => {
    if (err) {
      console.log(ERROR_MESSAGE, err);
    } else {
      console.log(value);
    }
  });
};

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.log(ERROR_MESSAGE, err);
    } else {
      console.log(reply);
      client.print(value);
    }
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
