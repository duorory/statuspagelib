from requests import request
import json
import config as conf

def getIDfromEmail(email):
  output = request('GET', conf.API_URL + conf.ENDPOINT, 
                   data={'subscriber[email]':str(email)})
  json_out = json.loads(output.content)
  if not json_out['subscribers']:
    print 'ID Not found for {} address'.format(email)
  else:
    subscriberId = json_out['subscribers'][0]['id']
    return subscriberId


def getIDbyComponentName(name):
    subComponent = []
    output = request('GET', conf.API_URL + conf.COMPONENTS_ENDPOINT)
    json_out = json.loads(output.content)
    for component in json_out['components']:
        if component['name'] == name:
            id = component['id']
    for component in json_out['components']:
        if component['group_id'] == id:
            subComponent.append(component['id'])
    if not subComponent:
        return None
    return subComponent


def updateSubscription(subscriberID, components):
  output = request('PATCH', conf.API_URL + conf.SUBSCRIBER_ENDPOINT.format(subscriberID),
                   data = {'subscriber[components][]':components})
  json_out = json.loads(output.content)
  return json_out
