# ✅ Dummy scraper for Render (No Selenium required)
def fetch_case_details(case_type, case_no, year):
    return {
        "status": "success",
        "parties": f"Case Type: {case_type}, Case No: {case_no}/{year}",
        "filing_date": "Not Available (Cloud Mode)",
        "next_hearing": "Not Available",
        "pdf_link": "https://example.com/sample_order.pdf",
        "raw_html": "<html>dummy response for Render</html>"
    }
