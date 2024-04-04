from datetime import datetime

# Funtion to print logs on console with details
def printLog(message: str) -> None:
    
    date_now: datetime = datetime.now()
    formatted_date: str = date_now.strftime("%d/%m/%Y")
    print('- Info App | ' + formatted_date + ': '+ message)