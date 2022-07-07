import requests
from datetime import datetime

print("Hello World!")
print("Testing CI/CD BNI")

response = requests.get("https://www.google.com")

print(response.text)

waktu = datetime.now()

with open("tempResponse/" + str(waktu) + ".txt", "w") as f:
    f.write(response.text)