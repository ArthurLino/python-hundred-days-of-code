import requests as req

def fetch_question_data() -> dict:
    response = req.get('https://opentdb.com/api.php', params={
        'amount': 10,
        'type': 'boolean',
    })
    response.raise_for_status()
    response = response.json()['results']

    return response

question_data = fetch_question_data()
