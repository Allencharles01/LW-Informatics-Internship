#Post on Instagram: Post a message on Instagram using Python.  

import requests
import time

# Step 1: Replace with your actual values
access_token = 'YOUR_LONG_LIVED_ACCESS_TOKEN'
instagram_account_id = 'YOUR_INSTAGRAM_BUSINESS_ACCOUNT_ID'
image_url = 'https://example.com/image.jpg'  # Must be public
caption = '📸 Posted using Python and Instagram Graph API! #Python #InstagramAPI'

# Step 2: Create media container
media_url = f"https://graph.facebook.com/v18.0/{instagram_account_id}/media"

media_payload = {
    'image_url': image_url,
    'caption': caption,
    'access_token': access_token
}

media_response = requests.post(media_url, data=media_payload)
media_result = media_response.json()

if 'id' not in media_result:
    print("❌ Failed to create media container:", media_result)
    exit()

creation_id = media_result['id']
print("🖼️ Media container created. ID:", creation_id)

# Step 3: Publish the post
time.sleep(2)  # Just to avoid any timing issues (optional but good)

publish_url = f"https://graph.facebook.com/v18.0/{instagram_account_id}/media_publish"
publish_payload = {
    'creation_id': creation_id,
    'access_token': access_token
}

publish_response = requests.post(publish_url, data=publish_payload)
publish_result = publish_response.json()

if 'id' in publish_result:
    print("✅ Post published successfully! Post ID:", publish_result['id'])
else:
    print("❌ Failed to publish:", publish_result)
