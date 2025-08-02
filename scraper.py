# scraper.py (for Render Deployment - Dummy Fallback)
import os

def fetch_case_details(case_type, case_no, year):
    # Render me Selenium not supported, so we return dummy data
    return {
        "status": "success",
        "parties": f"Case Type: {case_type}, Case No: {case_no}/{year}",
        "filing_date": "Not Available (Cloud Mode)",
        "next_hearing": "Not Available",
        "pdf_link": "https://example.com/sample_order.pdf",
        "raw_html": "<html>dummy response for Render</html>"
    }
