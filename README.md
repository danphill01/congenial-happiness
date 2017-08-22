# Bucket List API
The api enables you to create/ register a user within the application.

## Usage

### User registration.
Send a `POST` request to `auth/register` endpoint with the payload in
`Json`

An example would be
```
{"email":"example@gmail.com",
 "password": "123456"}
```

The email value must be a valid email format and the password must be
four characters and above.

If the email is invalid or empty and the password is empty or less than
four character, the response `status` will be `failed` with the `message`
`Missing or wrong email format or password is less than four characters`
and a `status code` of `202`