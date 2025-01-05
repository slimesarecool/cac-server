from flask import Flask
from flask import request as req
import random
import string

app = Flask(__name__)

SECRET = "h2OqwnGm51t5IGcZLdgkFigJepUgmwqC"

unverified = []
verified = []

def generateCode():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@app.get("/connect")
def connect():
    code = generateCode()
    unverified.append(code)
    return code

@app.post("/verify")
def verify():
    data = req.get_json()
    givenSecret = data.get("secret")
    robloxUsername = data.get("robloxUsername")
    code = data.get("code")

    if givenSecret != SECRET:
        return "Invalid Code!" # Actually an invalid secret. Uses a different message not to help others. ;)
    
    if code not in unverified:
        return "Invalid Code"
    
    verified.append(robloxUsername)
    unverified.remove(code)

    return "Verification Successful"

if __name__ == '__main__':
    app.run()