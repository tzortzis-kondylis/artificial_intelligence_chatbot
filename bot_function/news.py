import time
import requests


def news_select():
    message = {
        "text": "Select Category",
        "quick_replies": [{
            "content_type": "text",
            "title": "Sports",
            "image_url": "https://www.freeiconspng.com/uploads/baseball-ball-icon--sport-iconset--icons-land-25.png",
            "payload": "sports"
        },
            {
                "content_type": "text",
                "title": "Entertainment",
                "image_url": "http://www.myiconfinder.com/uploads/iconsets/256-256-c4d10995b44ddf1264603751227e97cb-entertainment.png",
                "payload": "entertainment"
            },
            {
                "content_type": "text",
                "title": "Science",
                "image_url": "https://webstockreview.net/images600_/experiment-clipart-science-equipment-1.png",
                "payload": "science"
            },
            {
                "content_type": "text",
                "title": "Technology",
                "image_url": "https://inexinc.com/wp-content/uploads/2019/10/blog-2019-10-15-001-1024x683.jpg",
                "payload": "technology"
            }

        ]
    }
    return message


def news_bot(category, recipient_id, bot):
    url = (
            'https://newsapi.org/v2/top-headlines?country=us&category=' + category + '&apiKey=c44169f8f0a84c7e8ad1bf42815e39b4')
    response = requests.get(url).json()
    var = response['articles']
    i = 0
    x = 0
    while i < 2:
        y = 0
        while y < 5:

            if var[x + y]['urlToImage'] is None or var[x + y]['urlToImage'] == '':
                var[x + y][
                    'urlToImage'] = 'https://www.bridgiot.co.za/wp-content/uploads/2018/12/1024x1024-no-image-available.png'

            if var[x + y]['description'] is None or var[x + y]['description'] == '':
                var[x + y]['description'] = 'No Description Available'

            y = y + 1

        elements = [
            {
                "title": "" + var[x]['source']['name'],
                "image_url": "" + var[x]['urlToImage'],
                "subtitle": "" + var[x]['description'],
                "buttons": [
                    {
                        "type": "web_url",
                        "url": "" + var[x]['url'],
                        "title": "Read More"
                    }
                ]
            },
            {
                "title": "" + var[x + 1]['source']['name'],
                "image_url": "" + var[x + 1]['urlToImage'],
                "subtitle": "" + var[x + 1]['description'],
                "buttons": [
                    {
                        "type": "web_url",
                        "url": "" + var[x + 1]['url'],
                        "title": "Read More"
                    }
                ]
            },
            {
                "title": "" + var[x + 2]['source']['name'],
                "image_url": "" + var[x + 2]['urlToImage'],
                "subtitle": "" + var[x + 2]['description'],
                "buttons": [
                    {
                        "type": "web_url",
                        "url": "" + var[x + 2]['url'],
                        "title": "Read More"
                    }
                ]
            },
            {
                "title": "" + var[x + 3]['source']['name'],
                "image_url": "" + var[x + 3]['urlToImage'],
                "subtitle": "" + var[x + 3]['description'],
                "buttons": [
                    {
                        "type": "web_url",
                        "url": "" + var[x + 3]['url'],
                        "title": "Read More"
                    }
                ]
            },
            {
                "title": "" + var[x + 4]['source']['name'],
                "image_url": "" + var[x + 4]['urlToImage'],
                "subtitle": "" + var[x + 4]['description'],
                "buttons": [
                    {
                        "type": "web_url",
                        "url": "" + var[x + 4]['url'],
                        "title": "Read More"
                    }
                ]
            }
        ]
        bot.send_generic_message(recipient_id, elements)
        time.sleep(1)
        x = x + 5
        i = i + 1

    return "success"
