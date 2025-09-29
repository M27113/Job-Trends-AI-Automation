# Job Trends AI Automation
Python | OpenAI GPT-4o-mini | Google Sheets API | Automation

**Automated AI-driven workflow for trending job notifications, content generation, and social media automation.**

I built an end-to-end AI-powered workflow that tracks trending job-related updates (admit cards, notifications, results), categorizes them automatically using GPT-4o-mini, and generates content for Instagram, blogs, YouTube reels, and thumbnails. The system updates a Google Sheet for review and is ready for scheduling and automation.

---

## 📌 Project Overview
This project automates:

1. **Data Extraction** – Collect trending job-related topics from Google Trends.
2. **Categorization** – Classify trends into Admit Card, Job Notification, Result, or Not Relevant using AI.
3. **Content Generation** – Generate Instagram posts, blogs, YouTube reels, and thumbnail ideas via GPT-4o-mini.
4. **Google Sheet Update** – Update trends and generated content for review or publishing.

**Purpose:** Build a portfolio-ready project showcasing AI, automation, and workflow integration skills.

---

## 🛠 Tech Stack
- **Python 3.11**  
- **Pytrends** – Trending data extraction  
- **OpenAI GPT-4o-mini** – AI categorization & content generation  
- **gspread & Google Sheets API** – Sheet management  
- **Scheduling/Automation** – Optional recurring updates  

---

## 📂 Folder Structure
    
    job-trends-ai/
    │
    ├─ phase1_data_extraction.py
    ├─ phase2_data_categorization.py
    ├─ phase3_content_generation.py
    ├─ credentials.json # Keep private
    └─ .env 
    ├─ requirements.txt
    └─ README.md

---

## ⚡ Quick Start
1. **Clone the repo:**  
    ```bash
    git clone https://github.com/yourusername/job-trends-ai.git
    cd job-trends-ai

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Set environment variable:**

   export OPENAI_API_KEY="your_openai_api_key"

4. **Configure Google Sheets:**

    - Place credentials.json in the repo root.
    
    - Share your sheet with the service account email.

5. **Run each phase:**

    - python phase1_data_extraction.py
    - python phase2_data_categorization.py
    - python phase3_content_generation.py

## 🏆 Highlights 

  - Full-stack AI Workflow: From data collection → categorization → content creation → Google Sheet update.
  
  - GPT Integration: Using GPT-4o-mini for real-world trend classification and content generation.
  
  - Automation Ready: Can be scheduled for repeated execution.
  
## 🔮 Future Improvements

  - Add direct social media publishing (Instagram, YouTube, Blog).
  
  - Include more trend categories and smarter AI categorization.
  
  - Cloud-based scheduled workflow for continuous automation.
  
  - Fine-tune GPT models for higher-quality content.

## 📸 Screenshots / Demo

  - Google Sheet with trends & categories
  
  - AI-generated Instagram post
  
  - Blog Draft Sample

## ⚠️ Notes

  - Keep credentials.json private.
  
  - GPT API usage may incur costs.
  
  - Google Sheet API must be enabled.
