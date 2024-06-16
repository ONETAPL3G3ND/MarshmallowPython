# https://github.com/ONETAPL3G3ND
from marshmallow import Schema, fields

class UserData(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    telephonenumbers = fields.Str(required=False)
    ip = fields.IPv4(required=True)

user_data = {
    "name": "Vasya",
    "email": "info@illuminatex.de",
    "ip": "192.168.0.1"
}

UserSchema = UserData()
user = UserSchema.load(user_data)

print(user)
