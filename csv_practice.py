#csv_practice.py
# Author: Logan Brady
# Module 12 lab: Read a Sales CSV, Write a cleaned report

import csv
from datetime import datetime

SALES_CSV = 'data/sales.csv'
CLEANED_CSV = 'data/cleaned_sales.csv'
LOG_FILE = 'data/sales_log.txt'

print("---Exercise 1---")
with open(SALES_CSV, 'r') as f:
    print(f"Opened {SALES_CSV} .")

print("---Exercise 2---")
with open(SALES_CSV, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

