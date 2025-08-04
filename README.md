# 🏛 Court Data Fetcher – Internship Project  
**Internship Organization:** Think Act Rise Foundation  

## 📌 Project Overview  
Court Data Fetcher is a **Flask-based web application** that allows users to search **Indian court case details** by entering:  
- **Case Type**  
- **Case Number**  
- **Filing Year**  

The app displays:  
- ✅ Parties’ Names  
- ✅ Filing Date  
- ✅ Next Hearing Date  
- ✅ Latest Order/Judgment PDF (if available)  

> ⚡ If the real court site is **CAPTCHA-protected or unreachable**, the app uses **Dummy Fallback Data** to ensure smooth functionality.

---

## 🎯 Key Features
- 🌐 **Responsive UI** (Bootstrap + Custom Styling)  
- 📊 **Admin Logs Dashboard** (Stores all search queries in SQLite)  
- 🔍 **Court Case Lookup** (Real-time scraping in local mode)  
- ☁️ **Cloud Deployment** on Render  
- 📑 **Court PDF Download Simulation** (for demo purposes)

---

## 🎈 CAPTCHA Handling Strategy
- CAPTCHA on official court websites **cannot be bypassed legally**.  
- ✅ **Local Mode:** Uses Selenium to scrape real data manually when CAPTCHA is solved by the user.  
- ✅ **Cloud Mode:** Uses **dummy fallback data** to maintain demo functionality and avoid legal/technical issues.  

---

## 🛠️ Tech Stack
| Layer         | Technology |
|---------------|------------|
| **Frontend**  | HTML5, CSS3, Bootstrap |
| **Backend**   | Python Flask |
| **Database**  | SQLite |
| **Scraping**  | Requests / Selenium (local) |
| **Deployment**| Render Cloud |

---

## 📂 Project Structure
Court-Data-Fetcher/
│── templates/ # HTML templates (index, result, logs, error)
│── static/ # CSS, JS, and optional assets
│── app.py # Main Flask app
│── scraper.py # Scraper logic (real + dummy)
│── requirements.txt # Dependencies
│── Procfile # For Render deployment
│── README.md # Project Documentation


---

## 🌐 Live Demo
- 🔗 **Web App:** [https://court-data-fetcher-p66k.onrender.com](https://court-data-fetcher-p66k.onrender.com)  
- 📱 **QR Code:** *(Attach QR Image here)*

---

## 🖼️ Screenshots
- Search Form UI  
- Case Details Output (with PDF link)  
- Logs Dashboard  

---

## 🚀 How to Run Locally
```bash
# Clone the repository
git clone https://github.com/poonamdxt06/Court-Data-Fetcher.git
cd Court-Data-Fetcher

# Create virtual environment & install dependencies
pip install -r requirements.txt

# Run Flask server
python app.py
Access the app at http://127.0.0.1:5000/

✅ Future Enhancements
API Integration with eCourts

Multi-Court Support

Secure User Authentication for Logs

📌 Notes
Due to CAPTCHA restrictions, real-time scraping on cloud is not possible.

Judges can test real scraping by running the project locally with Selenium enabled.

👩‍💻 Author
Poonam Dixit
📧 Email: poonamdxt06@gmail.com
🔗 GitHub: Court-Data-Fetcher
