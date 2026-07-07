import os
import csv
import json
import random
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

def create_csv_files(directory):
    # Employees CSV
    with open(os.path.join(directory, 'employees.csv'), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'FirstName', 'LastName', 'Email', 'Department', 'Salary'])
        departments = ['IT', 'HR', 'Finance', 'Marketing', 'Sales']
        for i in range(1, 51):
            writer.writerow([
                f'EMP{i:03}', 
                f'First{i}', 
                f'Last{i}', 
                f'emp{i}@company.local', 
                random.choice(departments), 
                random.randint(40000, 120000)
            ])
            
    # Transactions CSV
    with open(os.path.join(directory, 'transactions.csv'), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['TransactionID', 'Date', 'Amount', 'Status', 'AccountID'])
        statuses = ['Completed', 'Pending', 'Failed']
        for i in range(1, 101):
            date_str = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d')
            writer.writerow([
                f'TRX-{1000+i}',
                date_str,
                round(random.uniform(10.0, 5000.0), 2),
                random.choice(statuses),
                f'ACC{random.randint(100, 999)}'
            ])

def create_json_files(directory):
    # Config file
    config = {
        "appName": "RPA_Processor",
        "version": "1.0.0",
        "settings": {
            "maxRetries": 3,
            "timeoutMs": 5000,
            "logLevel": "DEBUG"
        },
        "endpoints": {
            "api": "https://api.example.com/v1",
            "auth": "https://auth.example.com/login"
        }
    }
    with open(os.path.join(directory, 'config.json'), 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)
        
    # User profiles
    for i in range(1, 4):
        profile = {
            "userId": f"USR{i:04}",
            "preferences": {
                "theme": "dark",
                "notifications": True
            },
            "roles": ["user", "viewer" if i % 2 == 0 else "editor"],
            "lastLogin": (datetime.now() - timedelta(hours=random.randint(1, 48))).isoformat()
        }
        with open(os.path.join(directory, f'user_profile_{i}.json'), 'w', encoding='utf-8') as f:
            json.dump(profile, f, indent=4)

def create_xml_files(directory):
    # Invoices
    for i in range(1, 4):
        root = ET.Element("Invoice")
        
        header = ET.SubElement(root, "Header")
        ET.SubElement(header, "InvoiceNumber").text = f"INV-{202400+i}"
        ET.SubElement(header, "Date").text = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
        
        customer = ET.SubElement(root, "Customer")
        ET.SubElement(customer, "Name").text = f"Customer {i} LLC"
        ET.SubElement(customer, "TaxID").text = f"TAX-{random.randint(10000, 99999)}"
        
        items = ET.SubElement(root, "Items")
        total = 0
        for j in range(1, random.randint(2, 5)):
            item = ET.SubElement(items, "Item")
            ET.SubElement(item, "Description").text = f"Service Component {j}"
            ET.SubElement(item, "Quantity").text = str(random.randint(1, 10))
            price = round(random.uniform(50.0, 500.0), 2)
            ET.SubElement(item, "UnitPrice").text = str(price)
            total += price
            
        ET.SubElement(root, "TotalAmount").text = str(round(total, 2))
        
        tree = ET.ElementTree(root)
        ET.indent(tree, space="\t", level=0)
        tree.write(os.path.join(directory, f'invoice_{i}.xml'), encoding="utf-8", xml_declaration=True)

def create_txt_files(directory):
    # Log files
    levels = ["INFO", "DEBUG", "WARN", "ERROR"]
    messages = [
        "Process started successfully",
        "Connecting to database...",
        "Connection timed out",
        "Data validation failed for row ID",
        "File not found in the specified path",
        "Batch processing completed",
        "User authentication successful",
        "Invalid credentials provided"
    ]
    
    for i in range(1, 6):
        with open(os.path.join(directory, f'system_log_{i}.txt'), 'w', encoding='utf-8') as f:
            current_time = datetime.now() - timedelta(days=5-i)
            for _ in range(random.randint(10, 30)):
                current_time += timedelta(minutes=random.randint(1, 60))
                level = random.choice(levels)
                msg = random.choice(messages)
                f.write(f"[{current_time.strftime('%Y-%m-%d %H:%M:%S')}] [{level}] {msg}\n")

if __name__ == "__main__":
    target_dir = r"c:\Users\amray\Downloads\Dummy Files"
    os.makedirs(target_dir, exist_ok=True)
    
    create_csv_files(target_dir)
    create_json_files(target_dir)
    create_xml_files(target_dir)
    create_txt_files(target_dir)
    
    print("Successfully generated dummy files in:", target_dir)
