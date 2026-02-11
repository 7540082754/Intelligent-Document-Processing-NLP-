import re

def extract_invoice(text):
    fields = {
        "invoice_number": r'invoice\s*no[:\-]?\s*(\w+)',
        "date": r'date[:\-]?\s*([\d/]+)',
        "total_amount": r'total[:\-]?\s*₹?\s*([\d,.]+)'
    }

    data = {}
    for key, pattern in fields.items():
        match = re.search(pattern, text)
        data[key] = match.group(1) if match else None

    return data