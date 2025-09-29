# Job Trends AI Automation
Python | OpenAI GPT-4o-mini | Google Sheets API | Automation

**Automated AI-driven workflow for trending job notifications, content generation, and social media automation.**

I built an end-to-end AI-powered workflow that tracks trending job-related updates (admit cards, notifications, results), categorizes them automatically using GPT-4o-mini, and generates content for Instagram, blogs, YouTube reels, and thumbnails. The system updates a Google Sheet for review and is ready for scheduling and automation.

---

## 📌 Project Overview

**Phase 1 – Data Extraction**
- Fetch trending job-related topics from Google Trends.
- Remove duplicate entries.
- Store data in a Google Sheet.

**Phase 2 – Trend Categorization**
- Categorize trends using GPT-4o-mini:
  - Admit Card
  - Job Notification
  - Result
  - Not Relevant
- Update the Google Sheet with categories.

**Phase 3 – Content Generation**
- Generate content for each trend and category:
  - Instagram Post (caption + hashtags)
  - Blog Draft (2–3 paragraphs + placeholder links)
  - YouTube Reel (caption + hashtags)
  - Thumbnail Idea
- Update the Google Sheet automatically.

**Phase 4 – Sheet Update**
- Append new trends.
- Skip duplicates.
- Maintain a `Status` column for tracking workflow progress.

**Phase 5 – Simulated Publishing**
- Update sheet entries with "Published" placeholders for trends marked `Approved`.
- Generates placeholder links for Instagram, Blog, Reel, and Thumbnail.
- Content remains in the sheet until manually approved.
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
    ├─ phase1_data_extraction.ipynb
    ├─ phase2_data_categorization.ipynb
    ├─ phase3_content_generation.ipynb
    ├─ ai_job_trends_workflow_publish.py
    ├─ credentials.json # Keep private
    └─ .env 
    ├─ requirements.txt
    └─ README.md

---

## ⚡ Quick Start
## ⚙️ Setup Instructions

1. **Clone the repository**
    ```bash
    git clone <your-repo-url>
    cd <repo-folder>
2. Create a virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate      # Windows
3. Install dependencies
    ```bash
    pip install -r requirements.txt
4. Setup Google Sheets API

    - Create a Google Service Account.
    
    - Download credentials.json.
    
    - Share your target Google Sheet with the service account email.

5. Configure environment variables

    Create a .env file:
    ```bash
    OPENAI_API_KEY=your_openai_api_key_here
   
6. Prepare Google Sheet
    - Ensure columns:
        Trend | Category | Instagram | Blog | Reel | Thumbnail | Status
    
    - Leave it empty initially; the script will populate it.
7. 🏃 Run the Full Pipeline
   ```bash
    python ai_job_trends_workflow_publish.py
   
- The script will:
    
    - Fetch trending job topics from Google Trends.
    
    - Categorize them using GPT-4o-mini.
    
    - Generate content for each trend.
    
    - Update the Google Sheet.
    
    - Simulate publishing for trends marked as Approved.

## 🏆 Highlights 

  - Full-stack AI Workflow: From data collection → categorization → content creation → Google Sheet update.
  
  - GPT Integration: Using GPT-4o-mini for real-world trend classification and content generation.
  
  - Automation Ready: Can be scheduled for repeated execution.
  
## 🔮 Future Improvements

  - Add direct social media publishing (Instagram, YouTube, Blog).
  - Add human approval workflow with notifications.
  - Include more trend categories and smarter AI categorization.
  - Cloud-based scheduled workflow for continuous automation.
  - Fine-tune GPT models for higher-quality content.

## 📸 Screenshort / Sample output

![Sample_output][/Job_Trends.png]

- you can find the sample output generated here : sample_output.xlsx

## ⚠️ Notes

  - Keep credentials.json private.
  
  - GPT API usage may incur costs.
  
  - Google Sheet API must be enabled.
