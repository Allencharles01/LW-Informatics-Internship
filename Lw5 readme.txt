Linux Task 5: Sending Email, WhatsApp Message, Tweet, and SMS via Terminal

Title: Use Command-Line Tools to Send Messages Across Multiple Platforms

Objective:
Send Email, WhatsApp messages, Tweets, and SMS from the Linux terminal using various CLI tools and APIs.

1. Send an Email (using mailutils or mutt):

Install:
    sudo apt install mailutils

Command:
    echo "This is the email body." | mail -s "Subject Here" recipient@example.com

Note:
- Configure SMTP with ssmtp or postfix for sending emails.

2. Send a WhatsApp Message (using Twilio API via Python):

Step 1: Install Twilio SDK:
    pip install twilio

Step 2: Python Script:
    from twilio.rest import Client

    account_sid = 'YOUR_SID'
    auth_token = 'YOUR_TOKEN'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hello from Linux Terminal via WhatsApp!',
        to='whatsapp:+91XXXXXXXXXX'
    )
    print(message.sid)

Note:
- You need to register on Twilio and configure WhatsApp sandbox.

3. Send a Tweet (using 't' CLI):

Install:
    gem install t

Authorize:
    t authorize

Tweet Command:
    t update "Tweeting from the Linux terminal!"

Note:
- Twitter API may require elevated access and developer account.

4. Send an SMS (using Twilio CLI):

Install Twilio CLI:
    npm install -g twilio-cli
    twilio login

Send SMS:
    twilio api:core:messages:create \
      --from "+1XXXXXXX" \
      --to "+91XXXXXXXXXX" \
      --body "SMS from Linux terminal!"

Summary Table:

| Platform     | Tool Used           | Notes                          |
|--------------|---------------------|---------------------------------|
| Email        | mail, mutt          | SMTP setup required             |
| WhatsApp     | Twilio API          | Requires sandbox setup          |
| Twitter      | t CLI, Tweepy       | API access needed               |
| SMS          | twilio-cli          | Needs Twilio SMS credentials    |

Conclusion:
With a bit of setup, Linux terminal becomes a powerful communication hub. These tools are ideal for automation, scripting, and integrating messaging into other Linux workflows.
