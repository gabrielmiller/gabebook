import falcon
import json
import logging

INVALID_CREDENTIALS_ERROR_MSG = 'Invalid Credentials.'
JWT_TOKEN_TTL = 60 * 60 * 24

def are_credentials_valid(requestBody, db):
    logging.error(requestBody)
    try:
        username = requestBody['doc']['username']
        password = requestBody['doc']['password']
    except:
        return False

    logging.error("username is " + username)
    logging.error("password is " + password)

    return True

def is_token_valid(token):
    return True

def has_token_expired(token):
    return False

class AuthenticationChecker(object):
    def authorize(self, req, resp, resource, params):
        """
        Called on entry/person endpoints
        Checks if the request has a valid JWT token.
        If no token, a 401 is returned.
        If invalid token, a 400 is returned.

        Token is invalid if...
           - it, when decrypted, parses to invalid json
           - it has expired
           - the request's remote ip has changed
           - ?? how can I make this more secure?
        """
        #if req.context['user'] is None:
        #    raise HTTPUnauthorized('Authentication Required', 'No credentials supplied')
        if req.context['Authorization'] is None:
            raise HTTPUnauthorized('Authentication Required', 'No credentials supplied')
        if not is_token_valid(req.context['Authorization']):
            raise falcon.HTTPBadRequest(description=INVALID_CREDENTIALS_ERROR_MSG)

class AuthenticationResource(object):
    def __init__(self, db):
        self.db = db

    def generateJwtToken(self):
        return "test"

    def on_post(self, req, resp):
        logging.error(req.get_header('X-Real-IP'))
        isValid = are_credentials_valid(req.context, self.db)

        if (isValid):
            # upsert to db a session with the host, including a timestamp that the connection was established
            resp.status = falcon.HTTP_200
            resp.body = json.dumps({
                "token": req.context['doc']#self.generateJwtToken()
            })
        else:
            resp.status = falcon.HTTP_401
            resp.body = INVALID_CREDENTIALS_ERROR_MSG
