from flask import Blueprint, request, json, make_response, jsonify
import os.path
import sys

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

tassha_api = Blueprint('tassha_app', __name__)

CLIENT_ACCESS_TOKEN = '314e5c7a6ca94d459386983ea985236c'


@tassha_api.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    # res = processRequest(req)

    # res = json.dumps(res, indent=4)
    # print(res)

    res = {
        "speech": "This is a test",
        "displayText": "This is display Text",
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


@tassha_api.route('/apiai/<string:query>', methods=['POST'])
def api_ai(query):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    apirequest = ai.text_request()

    apirequest.lang = 'en'

    apirequest.session_id = "somethin"

    if query:
        apirequest.query = query
    else:
        apirequest.query = "Hey Tassha"

    # response = apirequest.getresponse()

    response = json.loads(apirequest.getresponse().read().decode('utf-8'))
    # res = jsonify(response)

    status = response['status']['code']
    if status == 200:
        # Sending the textual response of the bot.
        return {"speech": response['result']['fulfillment']['speech']}

    else:
        res = {"speech": "Sorry, I couldn't understand that question"}
        return res

# def processRequest(req):
# if req.get("result").get("action") != "yahooWeatherForecast":
#     return {}
# baseurl = "https://query.yahooapis.com/v1/public/yql?"
# yql_query = makeYqlQuery(req)
# if yql_query is None:
#     return {}
# yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
# result = urlopen(yql_url).read()
# data = json.loads(result)
# res = makeWebhookResult(data)
# return res
