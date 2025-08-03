from bs4 import BeautifulSoup
import requests
import os

USE_DUMMY = os.getenv("USE_DUMMY", "true").lower() == "true"

def fetch_case_details(case_type, case_no, year):
    if USE_DUMMY:
        # ✅ Return fallback dummy data on Render
        return {
            "status": "success",
            "parties": f"Dummy Parties for {case_type} {case_no}/{year}",
            "filing_date": "Not Available (Cloud Mode)",
            "hearing_date": "Not Available",
            "order_link": "#",
            "raw_html": "<html>dummy</html>"
        }

    # ✅ Otherwise, perform actual scraping (local mode)
    try:
        url = "https://districts.ecourts.gov.in/faridabad"  # example
        # your scraping logic with requests/selenium here
        # parse response
        return {
            "status": "success",
            "parties": "Parsed Parties",
            "filing_date": "2024-01-10",
            "hearing_date": "2024-06-20",
            "order_link": "http://example.com/order.pdf",
            "raw_html": "<html>...</html>"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
