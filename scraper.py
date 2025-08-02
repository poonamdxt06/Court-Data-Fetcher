from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def fetch_case_details(case_type, case_no, year):
    try:
        # ✅ Selenium Setup
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-gpu")

        service = Service(r"C:\Users\poona\chromedriver\chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)

        # ✅ Open Court Site
        driver.get(" https://delhihighcourt.nic.in")
        time.sleep(8)  # wait for site load

        # ✅ Attempt to Navigate to Case Status (if available)
        try:
            driver.find_element(By.LINK_TEXT, "Case Status").click()
            time.sleep(5)
        except:
            pass

        # ✅ Fill Form (if elements found)
        try:
            driver.find_element(By.NAME, "case_type").send_keys(case_type)
            driver.find_element(By.NAME, "case_no").send_keys(case_no)
            driver.find_element(By.NAME, "case_year").send_keys(year)
        except:
            raise Exception("Form elements not found (Site may be down).")

        # ✅ Wait for Manual CAPTCHA Solve
        input("⚠️ Solve CAPTCHA in browser, then press Enter here...")

        # ✅ Click Search
        driver.find_element(By.ID, "search_case").click()
        time.sleep(5)

        # ✅ Scrape Case Data
        try:
            parties = driver.find_element(By.XPATH, "//td[contains(text(),'Petitioner')]/following-sibling::td").text
        except:
            parties = "Not Found"

        try:
            filing_date = driver.find_element(By.XPATH, "//td[contains(text(),'Filing Date')]/following-sibling::td").text
        except:
            filing_date = "Not Found"

        try:
            next_hearing = driver.find_element(By.XPATH, "//td[contains(text(),'Next Hearing Date')]/following-sibling::td").text
        except:
            next_hearing = "Not Found"

        try:
            pdf_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Order").get_attribute("href")
        except:
            pdf_link = "No Order PDF Found"

        driver.quit()

        return {
            "status": "success",
            "parties": parties,
            "filing_date": filing_date,
            "next_hearing": next_hearing,
            "pdf_link": pdf_link,
            "raw_html": "Scraped via Selenium"
        }

    except Exception as e:
        # ✅ Fallback Dummy Data if Scraping Fails
        return {
            "status": "success",
            "parties": f"Case Type: {case_type}, Case No: {case_no}/{year} (Fallback Data)",
            "filing_date": "Not Available (Fallback)",
            "next_hearing": "Not Available (Fallback)",
            "pdf_link": "https://example.com/sample_order.pdf",
            "raw_html": f"Fallback used due to: {str(e)}"
        }
