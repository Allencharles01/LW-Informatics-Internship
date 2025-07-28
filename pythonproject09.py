#Develop a menu-driven Python project: that combines all Python tasks into a single program.

import os
import time

# --- lw_project01: Send Email ---
def send_email():
    import smtplib
    from email.message import EmailMessage

    msg = EmailMessage()
    msg['Subject'] = 'Hello from Python!'
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = 'recipient_email@gmail.com'
    msg.set_content('Hey! This email was sent using Python.')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('your_email@gmail.com', 'your_app_password')
            smtp.send_message(msg)
        print("✅ Email sent!")
    except Exception as e:
        print("❌ Failed to send email:", e)

# --- lw_project02: Send SMS ---
def send_sms():
    import requests
    payload = {
        "sender_id": "FSTSMS",
        "message": "Hello from Python SMS script!",
        "language": "english",
        "route": "q",
        "numbers": "9123456789"
    }
    headers = {
        'authorization': 'YOUR_FAST2SMS_API_KEY',
        'Content-Type': "application/x-www-form-urlencoded"
    }
    response = requests.post("https://www.fast2sms.com/dev/bulkV2", data=payload, headers=headers)
    print(response.text)

# --- lw_project03: Make a Call ---
def make_call():
    from twilio.rest import Client
    client = Client("YOUR_TWILIO_SID", "YOUR_TWILIO_TOKEN")
    call = client.calls.create(
        to="+91XXXXXXXXXX",
        from_="+1415XXXXXXX",
        url="http://demo.twilio.com/docs/voice.xml"
    )
    print(f"📞 Call initiated! SID: {call.sid}")

# --- lw_project04: Post on LinkedIn ---
def post_linkedin():
    import requests, json
    access_token = 'YOUR_LINKEDIN_ACCESS_TOKEN'
    author_urn = 'urn:li:person:xxxxxxxx'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'X-Restli-Protocol-Version': '2.0.0',
        'Content-Type': 'application/json'
    }
    data = {
        "author": author_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": "Posted from Python 🚀"},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    res = requests.post("https://api.linkedin.com/v2/ugcPosts", headers=headers, data=json.dumps(data))
    print("✅ LinkedIn Post Created!" if res.status_code == 201 else f"❌ Failed: {res.text}")

# --- lw_project05: Post on Twitter ---
def post_tweet():
    import tweepy
    auth = tweepy.OAuth1UserHandler("API_KEY", "API_SECRET", "ACCESS_TOKEN", "ACCESS_SECRET")
    api = tweepy.API(auth)
    api.update_status("Tweeted using Python!")
    print("✅ Tweet posted!")

# --- lw_project06: Post on Facebook Page ---
def post_facebook():
    import requests
    token = "YOUR_PAGE_ACCESS_TOKEN"
    page_id = "YOUR_PAGE_ID"
    msg = "Hello from Python via Facebook API!"
    url = f"https://graph.facebook.com/{page_id}/feed"
    res = requests.post(url, data={"message": msg, "access_token": token})
    print("✅ Post Successful!" if res.status_code == 200 else f"❌ Failed: {res.text}")

# --- lw_project07: Post on Instagram ---
def post_instagram():
    import requests, time
    token = 'YOUR_IG_TOKEN'
    ig_id = 'YOUR_IG_ACCOUNT_ID'
    image_url = 'https://example.com/photo.jpg'
    caption = 'Instagram Post from Python!'
    create = requests.post(f'https://graph.facebook.com/v18.0/{ig_id}/media',
                           data={'image_url': image_url, 'caption': caption, 'access_token': token}).json()
    time.sleep(2)
    publish = requests.post(f'https://graph.facebook.com/v18.0/{ig_id}/media_publish',
                            data={'creation_id': create['id'], 'access_token': token}).json()
    print("✅ Instagram post published!" if 'id' in publish else f"❌ Failed: {publish}")

# --- lw_project08: Send WhatsApp Message ---
def send_whatsapp():
    import pywhatkit
    pywhatkit.sendwhatmsg("+91XXXXXXXXXX", "Hello from Python WhatsApp!", 14, 30)
    print("✅ WhatsApp message scheduled!")

# --- Menu Interface ---
def menu():
    while True:
        print("\n📍 Python Automation Hub")
        print("1. Send Email")
        print("2. Send SMS")
        print("3. Make a Phone Call")
        print("4. Post on LinkedIn")
        print("5. Post on Twitter")
        print("6. Post on Facebook Page")
        print("7. Post on Instagram")
        print("8. Send WhatsApp Message")
        print("9. Exit")

        choice = input("Select an option (1–9): ")

        if choice == '1': send_email()
        elif choice == '2': send_sms()
        elif choice == '3': make_call()
        elif choice == '4': post_linkedin()
        elif choice == '5': post_tweet()
        elif choice == '6': post_facebook()
        elif choice == '7': post_instagram()
        elif choice == '8': send_whatsapp()
        elif choice == '9':
            print("👋 Exiting. See you again!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

        input("\nPress Enter to return to the main menu...")

# Run the program
if __name__ == "__main__":
    menu()
