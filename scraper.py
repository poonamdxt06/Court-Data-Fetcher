import os
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://services.ecourts.gov.in/ecourtindia_v6/"  # Example court site

def fetch_case_details(case_type, case_no, year):
    # ✅ Toggle between dummy mode and real scraping using environment variable
    USE_DUMMY = os.getenv("USE_DUMMY", "true").lower() == "true"

    if USE_DUMMY:
        # ✅ Return dummy fallback data when running on cloud (Render)
        return {
            "status": "success",
            "parties": f"Case Type: {case_type}, Case No: {case_no}/{year}",
            "filing_date": "Not Available (Cloud Mode)",
            "next_hearing": "Not Available",
            "pdf_link": "https://example.com/sample_order.pdf",
            "raw_html": "<html>dummy</html>"
        }

    # ✅ If dummy mode is disabled, attempt real scraping (works only locally)
    try:
        payload = {
            "case_type": case_type,
            "case_no": case_no,
            "case_year": year,
        }
        res = requests.post(BASE_URL, data=payload, timeout=10)
        if res.status_code != 200:
            return {"status": "error", "message": "Court site unavailable"}

        soup = BeautifulSoup(res.text, "html.parser")
        parties = soup.find("div", class_="caseparty").get_text(strip=True)
        filing = soup.find("span", class_="filing_date").get_text(strip=True)
        next_hearing = soup.find("span", class_="next_hearing_date").get_text(strip=True)
        pdf_tag = soup.find("a", href=True, text="Order/Judgment")
        pdf_link = pdf_tag["href"] if pdf_tag else None

        return {
            "status": "success",
            "parties": parties,
            "filing_date": filing,
            "next_hearing": next_hearing,
            "pdf_link": pdf_link,
            "raw_html": res.text
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
