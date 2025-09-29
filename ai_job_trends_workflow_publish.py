# ai_job_trends_workflow_publish.py

import os
import gspread
from pytrends.request import TrendReq
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# ---------------------
# Setup
# ---------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("⚠️ Please set your OPENAI_API_KEY in environment variables")

client = OpenAI(api_key=OPENAI_API_KEY)

# Connect to Google Sheets
gc = gspread.service_account(filename="credentials.json")
sheet = gc.open("Job_Trends_Agent").sheet1

# ---------------------
# Phase 1: Fetch Trends
# ---------------------
def fetch_trends(keywords=None):
    if keywords is None:
        keywords = ["admit card", "job notification", "exam result"]
    pytrends = TrendReq(hl='en-US', tz=330)
    trending_data = []
    for kw in keywords:
        pytrends.build_payload([kw], cat=0, timeframe='now 7-d', geo='IN', gprop='')
        data = pytrends.related_queries()[kw]['top']
        if data is not None:
            trending_data.extend(data['query'].tolist())
    return list(set(trending_data))  # remove duplicates

# ---------------------
# Phase 2: Categorize Trends
# ---------------------
def categorize_trend(trend):
    prompt = f"""
You are an AI agent categorizing job-related trends. 
Classify the trend "{trend}" into one of the following:
- Admit Card
- Job Notification
- Result
- Not Relevant
Only reply with one category.
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()

# ---------------------
# Phase 3: Generate Content
# ---------------------
def generate_content(trend, category):
    prompt = f"""
You are a content creator. Based on the trend: "{trend}" (category: {category}),
generate the following:
1. Instagram Post: Short caption + 3-5 hashtags
2. Blog Draft: 2-3 paragraphs + placeholder link for the category
3. YouTube Reel: One-liner caption + 3-5 hashtags
4. Thumbnail Idea: Short catchy text
Separate each section with two newlines.
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip().split("\n\n")

# ---------------------
# Phase 4: Update Sheet
# ---------------------
def update_google_sheet():
    rows = sheet.get_all_values()
    header, data = rows[0], rows[1:]
    
    existing_trends = [row[0] for row in data]
    
    # Fetch new trends
    new_trends = fetch_trends()
    
    for trend in new_trends:
        if trend not in existing_trends:
            # Categorize trend
            category = categorize_trend(trend)
            # Skip if Not Relevant
            status = "Pending"
            sheet.append_row([trend, category, "", "", "", "", status])
            print(f"Added trend: {trend} | Category: {category} | Status: {status}")

    # Generate content for Pending & Approved trends
    rows = sheet.get_all_values()
    for i, row in enumerate(rows[1:], start=2):  # skip header
        trend, category, insta, blog, reel, thumb, status = row
        if category != "Not Relevant" and not insta:
            print(f"Generating content for: {trend} ({category})")
            content = generate_content(trend, category)
            sheet.update(f"C{i}", [[content[0]]])
            sheet.update(f"D{i}", [[content[1]]])
            sheet.update(f"E{i}", [[content[2]]])
            sheet.update(f"F{i}", [[content[3]]])
            print(f"✅ Content added for row {i}")

# ---------------------
# Phase 5: Simulate Publishing
# ---------------------
def publish_content():
    rows = sheet.get_all_values()
    for i, row in enumerate(rows[1:], start=2):
        trend, category, insta, blog, reel, thumb, status = row
        if status == "Approved":
            # Generate placeholder links
            sheet.update(f"C{i}", [[f"{insta} (Published Link)"]])
            sheet.update(f"D{i}", [[f"{blog} (Published Link)"]])
            sheet.update(f"E{i}", [[f"{reel} (Published Link)"]])
            sheet.update(f"F{i}", [[f"{thumb} (Published Link)"]])
            sheet.update(f"G{i}", [["Published"]])
            print(f"📢 Published trend: {trend}")

# ---------------------
# Main Pipeline
# ---------------------
if __name__ == "__main__":
    update_google_sheet()
    print("🎉 Trends categorized and content generated.")
    print("✅ Now you can manually set Status = 'Approved' in the sheet to publish content.")
    publish_content()
    print("🎉 Simulated publishing complete.")
