from parsers.pdf_parser import parse_pdf

result = parse_pdf("test_data/task3_high_risk.pdf")

print("Pages:", result["page_count"])
print("Keywords found:", result["risk_keywords_found"])
print("Litigation risk:", result["litigation_risk"])
print("Has risk?", result["has_risk"])