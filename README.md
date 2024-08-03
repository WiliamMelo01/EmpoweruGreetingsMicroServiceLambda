# EmpowerU Greetings Microservice

## Overview

The EmpowerU Greetings Microservice is designed to send welcome emails to new users. This service is implemented as an AWS Lambda function using Python and triggers on messages from an SQS queue.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Usage](#usage)
- [License](#license)
- [TODO](#todo)

## Features

- Listens to an SQS queue for new user registrations
- Sends a welcome email to the new user

## Technologies

- AWS Lambda
- Python
- AWS SQS (for triggering the function)

## Usage

The microservice listens to an SQS queue for messages. When a message is published to the queue, the Lambda function is triggered, and it reads the email address from the message body. The function then uses the `EmailService` to send a welcome email to the specified address.

### Example Workflow

1. A new user registers, and their email address is published to the SQS queue.
2. The Lambda function is triggered by the SQS message.
3. The function retrieves the email address from the message body.
4. It sends a welcome email to the provided address using the `EmailService`.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/WiliamMelo01/EmpoweruGreetingsMicroServiceLambda/blob/main/LICENSE) file for details.

## TODO

- [ ] Implement CI/CD to automate deploy
- [ ] Review email sending logic and handle potential edge cases
- [ ] Improve error handling and logging for production readiness
