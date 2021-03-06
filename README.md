# Dev setup

1. Install Python 3.8+ 
1. Run `pip install -r requirements.txt`
1. Run dev/getSecrets.py
1. When prompted, login to your Azure Active Directory account that you've had Tawnos associate with Key Vault
1. Copy the returned value into __app__/local.settings.json under API_KEY

# Objects, Enums, etc

```json

voteType: ['Deck','Topping']

// Represents a single submission of a user's vote, deducting from their total available votes based on SUM(donation.Amount)
vote: {<voteType>: count}

donation: { 'user_id': '<pledgeling:donation.user_id>', 'display_name':  'amount': '<pledgeling:donation.amount>' }

```

# API Thoughts

```json
POST /donate
=> <pledgeling.donate>

GET /user/{id}/votes
=>
{
    'UserId':'{id}'
}
<=
{
    'VotesLeft': 5
    'Votes': [<vote>]
}

GET /vote
<=
{
    'DeckVotes': [<vote> ,{}...],
    'ToppingVotes': [{},{}...],
}


    'TwitchName': '<twitch_name>',

POST /vote
=>
{
    "id": <voteid>,
    "user_id": <user_object>,
    "toppings": [
        {
            "Count": 4,
            "Value": ["ham", "pineapple"]
        },
        {
            "Count": 1,
            "Value": ["abc","def"]
        }
    ],
    "decks": [
        {
            "Count": 1
            "Value": <mtggoldfish_deck_id> => https://www.mtggoldfish.com/deck/<mtggoldfish_deck_id>
        }
    ]
}
<=
{
    "remaining_votes": {
        "toppings": 2
        "decks": 4
    }
}

POST/GET /goals
<=>
{
    'Goals': [{'amount':1000, 'extra': 'foo bar baz prize'}, {'amount':2000, 'extra': 'foo bar baz prize'}]
}

// _if time permits_ (else manually edited)
PATCH /admin/goals
=>
{
    'add': [{'amount':1000, 'extra': 'foo baz prize'}],
    'remove': [{'amount':1000, 'extra': 'foo bar baz prize'}]
}
```


# From Pledgeling

```
headers = { "Authorization": "Bearer {api_key}" }
r = requests.get(
  "https://api.pledgeling.com/v1/donations",
  headers=headers
  )

Donation POST
{
  "id": "0f69319c-9321-4531-ad52-6cb87a292d35",
  "user_id": "0854c837-b204-4ba0-8b39-238cb40ca7e9",
  "email": "btyrese@gmail.com",
  "first_name": "Brock",
  "last_name": "Tyrese",
  "organization_id": "3685b542-61d5-45da-9580-162dca725966",
  "organization_name": "American Red Cross",
  "amount": "0.25",
  "phone_number": "+13235550107",
  "status": "processed",
  "external_id": "439087218",
  "metadata": "arbitrary data string",
  "created_at": "2016-01-01T12:00:00Z",
  "updated_at": "2016-01-01T12:00:00Z"
}

Donation Webhook (filtered to fields)
{
  "topic": "donation/created",
  "data":  {
    "id": "940ff61f-91d1-4dce-98d2-cf1b1284793c",
    "user_id": "d913d990-3627-4cdf-b21b-e5dffc91bcc2",
    "organization_id": "dd959794-d83f-4128-be24-651d2a398f12",
    "organization_name": "Water.org",
    "amount": "0.68",
    "metadata": "arbitrary data string",
    "created_at": "2016-01-01T12:00:00Z",
  }
}
```
