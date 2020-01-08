# Python libraries that we need to import for our bot
from flask import Flask, request
from pymessenger.bot import Bot
from bot_funcions import news
from bot_funcions import learn
from bot_funcions import chatbot

ACCESS_TOKEN = 'EAAJPFDMf0QoBAMi6VXfpDKRZBZAdfgQXDXFKpM40U0YAdUV07PZCVKi67p7Kwu7UZAaZAvtUN8H5hbUuRs7Y0rAU3Oh9Hz4lsZBf2L3aXvMmzHEM531w0vLUY9Iy2AEZAQ3j4Cox7EKjNjwVKa1szLaVXSq03Y2FQWe1WuoDBBxOwZDZD'
VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)

learn.machine()
app = Flask(__name__)


# We will receive messages that Facebook sends our bot at this endpoint
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    # if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    # Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        var = message['message'].get('text')
                        response_sent_text = chatbot.chat(var)
                        send_message(recipient_id, response_sent_text)
                    # if user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        response_sent_nontext = 'I cannot understand this :( '
                        send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    # take token sent by facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


# uses PyMessenger to send response to user
def send_message(recipient_id, response):
    # sends user the text message provided via input response parameter
    action = {
        "recipient": {
            "id": "" + recipient_id
        },
        "sender_action": "typing_on"
    }
    bot.send_raw(action)
    if response in ['technology', 'sports', 'science', 'entertainment']:
        news.news_bot(response, recipient_id)
        bot.send_text_message(recipient_id, 'Anything else?')
    else:
        bot.send_message(recipient_id, response)
        bot.send_text_message(recipient_id, response)

    return "success"


if __name__ == "__main__":
    app.run()
