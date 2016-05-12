import beatbox
import datetime
import json
import config as conf


sf = beatbox._tPartnerNS
svc = beatbox.PythonClient()
svc.serverUrl = conf.SALESFORCE_ENDPOINT
svc.login(conf.SALESFORCE_LOGIN, conf.SALESFORCE_PASSWORD + conf.SALESFORCE_TOKEN)


def get_updated_deployments(num_days):
  field_history_query = "SELECT AccountId, OldValue, NewValue FROM AccountHistory WHERE Field = 'Deployment_Id__c' AND CreatedDate = LAST_N_DAYS:" + str(num_days)
  
  print "getting updated deployment contacts from salesforce..."
  res_acct = svc.query(field_history_query)
  print str(len(res_acct)) + " account(s)"
  return_list = []  

  for item in res_acct:
    print "\tAccountId: " + item['AccountId']
    print "\tOldDeploymentId: " + item['OldValue']
    print "\tNewDeploymentId: " + item['NewValue']
    return_list.append([get_account_contacts(item['AccountId'], item['OldValue'], item['NewValue'])])
  return return_list
    

def get_account_contacts(account_id, old_deployment, new_deployment):
  contact_query = "SELECT Contact.Email FROM Contact WHERE Contact.Account.Id = '" + account_id + "'"
  acct_contacts = []
  print "\tgetting contact(s) for account..."
  res_cnt = svc.query(contact_query)
  if res_cnt:
    print "\t\t" + str(len(res_cnt)) + " contacts"
    for item in res_cnt:
      print "\t\tContactEmail: " + str(item['Email'])
      acct_contacts.append([str(item['Email']), old_deployment, new_deployment])
  return acct_contacts
