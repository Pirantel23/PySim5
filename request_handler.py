import requests

session = None

def get_session():
    global session
    if session is None:
        session = requests.Session()
    return session

def send_request(url, headers: dict = None) -> dict:
    session = get_session()
    
    response = session.get(url, headers=headers)
    response.raise_for_status()
    # Process the response data and return it
    return response.json()