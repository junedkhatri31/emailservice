
# emailservice

This email service will handle all of your email sending for you. This application use [mailc](./mailc/) library to send emails internally.

## API Reference

#### Send an email

```http
  POST /message
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `from` | `string` | **Required**. email address from the email will be sent |
| `to` | `string` | **Required**. email address to the email will be sent |
| `subject` | `string` | **Required**. Subject of email address |
| `message` | `string` | **Required**. Email message body |

