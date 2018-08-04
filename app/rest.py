import web
import json
import os

urls = (
    '/login/', 'ValidateUsers',
)


ACCOUNTS_DATA = json.loads(open(os.path.join(os.getcwd(), 'accounts.json'), "r").read())


def search_user(email, password):
    """
    Go through the document looking for matche.
    Args:
        email: username.
        password: Gain access to the web site options
    Returns:
        JSON response with the user found.
    """
    find_user = dict()
    for user in ACCOUNTS_DATA["users"]:
        if user["email"] == email and user["password"] == password:
            find_user = {"email": user["email"], "name": user["name"]}
    return find_user
            

class ValidateUsers(object):
    def POST(self):
        """
        Get the information from the web data (JSON Format) to change to a dictionary.
        Args:
            email: username.
            password: Gain access to the web site options
        Returns:
            The user found information in a JSON format.
        """
        web.header('Content-Type', 'application/json')
        message = {"response": ""}
        try:
            data = json.loads(web.data())
            user = search_user(data["email"], data["password"])
            if len(user) == 0:
                message["response"] = "We cannot find an account with that information"
            else:
                message["response"] = "Hi {} welcome to Amazon!".format(user["name"])

        except KeyError:
            message["response"] = "Error: Invalid json provided"
        
        return json.dumps(message)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()