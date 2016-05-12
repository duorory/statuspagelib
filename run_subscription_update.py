import status_page as sp
import salesforce as sf


#Get Salesforce Accounts and Contacts with updated deployments in last day
accounts_to_update = sf.get_updated_deployments(1)

#Update StatusPage 
# TODO: Loop through SF result list and make updates against statuspage

for account in accounts_to_update:
  print str(account[0][0][0])
  subscriberID = sp.getIDfromEmail(str(account[0][0][0]))
  print subscriberID
  print str(account[0][0][2])
  componentID = sp.getIDbyComponentName(str(account[0][0][2]))
  print componentID
  if componentID is not None:
    componentID = sp.getIDbyComponentName(str(account[0][0][2]))
    print sp.updateSubscription(subscriberID, componentID)
  else:
    pass
