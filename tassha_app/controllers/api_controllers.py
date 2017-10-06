from flask import Blueprint, request, json, make_response

tassha_api = Blueprint('tassha_app', __name__)


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

