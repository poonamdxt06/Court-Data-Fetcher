import os
import requests
from bs4 import BeautifulSoup

# ✅ Environment flag to use dummy data when CAPTCHA/site blocks
USE_DUMMY = os.getenv("USE_DUMMY", "true").lower() == "true"

def fetch_case_details(case_type, case_no, year):
    # ✅ If dummy mode is ON → return sample data
    if USE_DUMMY:
        return {
            "status": "success",
            "case_type": case_type,
            "case_no": case_no,
            "year": year,
            "parties": "Dummy Party A vs Dummy Party B",
            "filing_date": "Not Available (Cloud Mode)",
            "next_hearing": "Not Available",
            "pdf_link": "#",
            "raw_html": "<html><body>Dummy Data Mode Enabled</body></html>"
        }

    try:
        # ✅ Replace this with actual scraping logic for real court site
        url = f"https://districts.ecourts.gov.in/search?type={case_type}&number={case_no}&year={year}"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return {"status": "error", "message": "Court site not reachable", "raw_html": response.text}

        soup = BeautifulSoup(response.text, "html.parser")

        # ✅ Example parsing logic (update selectors for real site)
        parties = soup.find("div", class_="partyNames").text.strip() if soup.find("div", class_="partyNames") else "Not Found"
        filing_date = soup.find("span", class_="filingDate").text.strip() if soup.find("span", class_="filingDate") else "Not Found"
        next_hearing = soup.find("span", class_="nextHearing").text.strip() if soup.find("span", class_="nextHearing") else "Not Found"
        pdf_link = soup.find("a", class_="latestOrder")["href"] if soup.find("a", class_="latestOrder") else "#"

        return {
            "status": "success",
            "case_type": case_type,
            "case_no": case_no,
            "year": year,
            "parties": parties,
            "filing_date": filing_date,
            "next_hearing": next_hearing,
            "pdf_link": pdf_link,
            "raw_html": response.text
        }

    except Exception as e:
        return {"status": "error", "message": str(e), "raw_html": ""}
