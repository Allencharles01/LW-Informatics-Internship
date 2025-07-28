import requests
import json

# Replace with your actual values
access_token = 'YOUR_ACCESS_TOKEN'  # OAuth token with 'w_member_social' permission
author_urn = 'urn:li:person:YOUR_PERSON_URN'  # Usually starts with 'urn:li:person:'

# LinkedIn API endpoint for sharing posts
url = 'https://api.linkedin.com/v2/ugcPosts'

headers = {
    'Authorization': f'Bearer {access_token}',
    'X-Restli-Protocol-Version': '2.0.0',
    'Content-Type': 'application/json'
}

post_data = {
    "author": author_urn,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "🚀 Just posted on LinkedIn using Python! #Python #Automation #LinkedInAPI"
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

response = requests.post(url, headers=headers, data=json.dumps(post_data))

if response.status_code == 201:
    print("✅ Post successfully created on LinkedIn!")
else:
    print("❌ Failed to post:", response.status_code)
    print(response.text)
