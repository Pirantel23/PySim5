import requests

session = None

def get_session() -> requests.Session:
    global session
    if session is None:
        session = requests.Session()
    return session

def send_request(url, headers: dict = None) -> dict:
    session = get_session()
    
    response = session.get(url, headers=headers)
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return response.text