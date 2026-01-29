#!/usr/bin/env python3
"""
Table-Tailor: CSV Data Formatter
Demonstrates: File handling, Data Cleaning, and CSV Transformation.
"""

import csv
import os

def format_data(input_file):
    if not os.path.exists(input_file):
        # Create dummy data if file doesn't exist for the demo
        with open(input_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Email", "Spent"])
            writer.writerow(["john doe", "JOHN@GMAIL.COM", "150.5"])
            writer.writerow(["jane smith", "Jane@Yahoo.com", "300"])

    output_file = "cleaned_data.csv"
    
    with open(input_file, 'r') as csv_in, open(output_file, 'w', newline='') as csv_out:
        reader = csv.DictReader(csv_in)
        writer = csv.DictWriter(csv_out, fieldnames=reader.fieldnames)
        writer.writeheader()
        
        for row in reader:
            # Clean data: Proper Case names, lowercase emails, round spending
            row["Name"] = row["Name"].title()
            row["Email"] = row["Email"].lower()
            row["Spent"] = f"${float(row['Spent']):,.2f}"
            writer.writerow(row)
            
    print(f"Data cleaned successfully! Saved to {output_file}")

if __name__ == "__main__":
    format_data("raw_data.csv")
