import requests

x=requests.get("https://www.fast2sms.com/dev/bulk?authorization=Y6PcQM1uV8Rf2LzI0xerS3vdFEmyatJ5gBlGCAo7WNUZsjkHKOIqM2XYwLKWdET0Ng9ar6tlyjGVe7Dm&sender_id=FSTSMS&message=This%20is%20message%20from%20python&language=english&route=p&numbers=9925393973")

print(x.text)

