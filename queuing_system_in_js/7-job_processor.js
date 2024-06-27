// this file is used to create a kue job processor

const kue = require('kue');
const queue = kue.createQueue();

const blacklistedNumbers = [
  '4153518780',
  '4153518781'
];

const sendNotification = (phoneNumber, message, job, done) => {
  if (blacklistedNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(0, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    job.progress(50, 100);
    done();
  }
};

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
