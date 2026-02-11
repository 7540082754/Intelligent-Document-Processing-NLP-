from ocr.ocr_engine import extract_text
from nlp.text_cleaner import clean_text
from classification.document_classifier import predict
from extraction.invoice_extractor import extract_invoice

def process_document(path):
    text = extract_text(path)
    text = clean_text(text)

    doc_type = predict(text)

    result = {"document_type": doc_type}

    if doc_type == "invoice":
        result.update(extract_invoice(text))

    return result

if __name__ == "_main_":
    output = process_document("data/raw/invoice1.png")
    print(output)