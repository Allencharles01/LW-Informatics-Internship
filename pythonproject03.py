#Make a Phone Call: Use Python to make a phone call.

from twilio.rest import Client

# Your Twilio credentials (get them from https://www.twilio.com/console)
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Initialize client
client = Client(account_sid, auth_token)

# Call details
from_number = '+1415XXXXXXX'  # Your Twilio phone number (must be purchased or trial-verified)
to_number = '+91XXXXXXXXXX'   # Indian phone number (include +91 country code)

# Make the call
call = client.calls.create(
    to=to_number,
    from_=from_number,
    url='http://demo.twilio.com/docs/voice.xml'  # TwiML URL for voice message
)

print(f"📞 Call initiated! SID: {call.sid}")
