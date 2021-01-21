import json
import requests
import csv


def create_csv(customer):
    csv_columns = ['device_id','port_id','ifIndex','ifName'] 
    csv_file = "file for csv"

    port_for_bill, json_ports = get_ports(customer)
    
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in json_ports:
            writer.writerow(data)

def api_settings(customer):
    api_token = 'put api key here'
    api_url_base = 'https://librenms.org/api/v0/'
    api_port_uri = 'ports/search/Cust:%20'
    api_bill_uri = 'bills'
    api_customer = customer
    combined_port_url = api_url_base + api_port_uri + api_customer
    combined_bill_uri = api_url_base + api_bill_uri
    headers2={'X-Auth-Token': api_token}
    return combined_port_url, headers2, combined_bill_uri

def bill_fields():
    bill_name = input('What is the name of the bill? ')
    bill_day = '1'
    bill_type = 'cdr'
    bill_cdr = int(input('What is the new CDR? '))*1000000000
    bill_custid = input('What is the customerID? ')
    bill_ref = input('Who is the reference? ')
    bill_notes = input('Notes for the bill: ')
    return bill_name, bill_day, bill_type, bill_cdr, bill_custid, bill_ref, bill_notes 

def get_ports(customer):
    url, headers, bill = api_settings(customer)

    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            jsondata = json.loads(response.content.decode('utf-8'))
            json_ports = jsondata['ports']
    except:
        print("The API couldn't be resolved")

    ports_for_bill = []

    for val in json_ports:
            temp_ports = val['port_id']
            ports_for_bill.append(temp_ports)

    return ports_for_bill, json_ports

    
def create_new_bill(customer):
    url, headers, billing_api_uri = api_settings(customer)
    bill_name, bill_day, bill_type, bill_cdr, bill_custid, bill_ref, bill_notes = bill_fields()

    ports_for_bill, json_ports = get_ports(customer)

    payload = {
        "ports": ports_for_bill,
        "bill_name": bill_name,
        "bill_day": bill_day,
        "bill_type": bill_type,
        "bill_cdr": bill_cdr,
        "bill_custid": bill_custid,
        "bill_ref": bill_ref,
        "bill_notes": bill_notes
     }
    r = requests.post(billing_api_uri, data=json.dumps(payload), headers=headers)
    
def update_bill(customer, bill_id):
    url, headers, billing_api_uri = api_settings(customer)

    ports_for_bill, json_ports = get_ports(customer)
    update_payload = { 
        "ports": ports_for_bill,
        "bill_id": bill_id,
    }
    r2 = requests.post(billing_api_uri, data=json.dumps(update_payload), headers=headers)
    print(r2.content)



create_new_bill('Customer Name')
update_bill('Customer Name', put bill_id here)
create_csv('Customer Name')
