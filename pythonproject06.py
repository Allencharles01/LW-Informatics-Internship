#Post on Facebook: Use Python to post or share data on Facebook.   

import requests

# Replace with your page access token and page ID
page_access_token = 'YOUR_PAGE_ACCESS_TOKEN'
page_id = 'YOUR_PAGE_ID'
message = '🚀 Posting to Facebook Page using Python! #Python #Automation #FacebookAPI'

# Facebook Graph API endpoint
url = f'https://graph.facebook.com/{page_id}/feed'

payload = {
    'message': message,
    'access_token': page_access_token
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print("✅ Post successfully published to Facebook Page!")
else:
    print(f"❌ Failed to post: {response.status_code}")
    print(response.text)
