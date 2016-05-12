import status_page as sp
import salesforce as sf


#Get Salesforce Accounts and Contacts with updated deployments in last day
accounts_to_update = sf.get_updated_deployments(1)

#Update StatusPage 
# TODO: Loop through SF result list and make updates against statuspage
print sp.getIDfromEmail('rory.ramtech@gmail.com')

