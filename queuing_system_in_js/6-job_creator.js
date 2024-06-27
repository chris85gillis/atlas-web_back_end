// this file is used to create a kue job

const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '123456789',
  message: 'Hello, world!',
};

const job = queue.create('push_notification_code', jobData).save((err) => {
  if (err) {
    console.log('Error creating job:', err);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});

queue.on('job complete', (id, result) => {
  console.log(`Notification job completed: ${id}`);
});

queue.on('job failed', (id, errorMessage) => {
  console.log(`Notification job failed: ${id} with error ${errorMessage}`);
});
