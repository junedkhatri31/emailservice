
# mailc

Mailc is a simple mail library that supports failover. Mailc will send mail according to the settings you supply. It takes a list of SMTP setups as input. It will begin with the first configuration, and if that fails, it will move on to the next configuration, and so on. The exception `mailc.exceptions.MailNotSentError` will be thrown if all other configurations fail.


## Installation

Install mailc with pip

```bash
  pip install mailc
```
    
## Environment Variables

### For non-django project
To run this project, you will need to add the following environment variable as JSON and minified formatted.

`MAILC_EMAIL_BACKENDS`

eg.,
For the following configurations,
```json
[
  {
    "HOST": "smtp1.exmaple.com",
    "PORT": 587,
    "USERNAME": "smtp1user",
    "PASSWORD": "xxxxxxx"
  },
  {
    "HOST": "smtp2.exmaple.com",
    "PORT": 587,
    "USERNAME": "smtp2user",
    "PASSWORD": "xxxxxxx"
  }
]
```

Environment should be initialized as below,
```
export MAILC_EMAIL_BACKENDS='[{"HOST":"smtp1.exmaple.com","PORT":587,"USERNAME":"smtp1user","PASSWORD":"xxxxxxx"},{"HOST":"smtp2.exmaple.com","PORT":587,"USERNAME":"smtp2user","PASSWORD":"xxxxxxx"}]'
```

### For django project

If you are using django then it should belongs to your [django settings](https://docs.djangoproject.com/en/4.0/topics/settings/)
This settings must be list of dictionaries.
```python
MAILC_EMAIL_BACKENDS = [
  {
    "HOST": "smtp1.exmaple.com",
    "PORT": 587,
    "USERNAME": "smtp1user",
    "PASSWORD": "xxxxxxx"
  },
  {
    "HOST": "smtp2.exmaple.com",
    "PORT": 587,
    "USERNAME": "smtp2user",
    "PASSWORD": "xxxxxxx"
  }
]

``` 


## Usage

```python
from mailc import send_mail
from email.message import EmailMessage

message = EmailMessage()
message['From'] = 'fromemail@exmaple.com'
message['To'] = 'toemail@exmaple.com'
message['Subject'] = 'This is a subject'
message.set_content("This is message content")

send_mail(message)
```

