#Send an SMS: Send a text message using Python.   
import requests

url = "https://www.fast2sms.com/dev/bulkV2"

payload = {
    "sender_id": "FSTSMS",
    "message": "Hey! This is a test SMS from my Python app 🐍📲",
    "language": "english",
    "route": "q",  # Use 'q' for quick transactional messages
    "numbers": "0123456789"  #Replace with your recipient's number
}

headers = {
    'authorization': 'ENTER YOUR API KEY',  # Replace with your actual API Key
    'Content-Type': "application/x-www-form-urlencoded"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)