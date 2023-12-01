import requests

def convert_curr():
    init_currency = input("Enter the initial currency: ")
    target_currency = input("Enter the target currency: ")
    
    while True:
        try:
            amount = float(input('Enter the Amount: '))
        except:
            print('the amount needs to be numeric')
            continue
       
        if not amount > 0:
            print('Amount needs to be greater than 0')
            continue
        else:
            break
    
    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"

    payload = {}
    headers= {
    "apikey": "0vwfBoQTfWCbhCKpJq1wi6DOKHNL7Y3W"
}

    response = requests.request("GET", url, headers=headers, data = payload)
    status_code = response.status_code
    result = response.json()
    if status_code != 200:
        
        print("Error Response:" + str(result))
        quit()
    
    result = response.json()
    print('Conversion Result: ' + str(result['result']))
          
if __name__ == '__main__':
    convert_curr()
