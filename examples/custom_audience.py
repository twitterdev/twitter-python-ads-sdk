import hashlib
from twitter_ads.client import Client
from twitter_ads.audience import CustomAudience

CONSUMER_KEY = 'your consumer key'
CONSUMER_SECRET = 'your consumer secret'
ACCESS_TOKEN = 'access token'
ACCESS_TOKEN_SECRET = 'access token secret'
ACCOUNT_ID = 'account id'

# initialize the client
client = Client(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# load the advertiser account instance
account = client.accounts(ACCOUNT_ID)

# create a new custom audience
audience = CustomAudience.create(account, 'test CA')

# sample user
# all values musth be sha256 hashed
email_hash = hashlib.sha256("test-email@test.com").hexdigest()

# create payload
user = [{
    "operation_type": "Update",
    "params": {
        "users": [{
            "email": [
                email_hash
            ]
        }]
    }
}]

# update the custom audience
success_count, total_count = audience.users(user)
if success_count == total_count:
    print(("Successfully added {total_count} users").format(total_count=total_count))
