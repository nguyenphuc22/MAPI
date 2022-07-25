import win32com.client
#other libraries to be used in this script
import os
from datetime import datetime, timedelta

outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")

for account in mapi.Accounts:
	print(account.DeliveryStore.DisplayName)

