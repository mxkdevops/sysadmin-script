import pandas as pd
import os

# Example path
folder = r"C:\Users\km443\OneDrive\Desktop\plan"
file_path = os.path.join(folder, "output.xlsx")

# Define the sample data
data = {
    "Skill Area": ["Linux Logs", "AI Prompts", "AWS Infra", "DevOps", "Web Dev"],
    "Week(s)": ["1", "3", "2, 7", "4, 6", "2, 4"],
    "Tool / Topic": [
        "Log Analyzer CLI, syslog, journald",
        "OpenAI Prompt Engineering",
        "Lightsail, EC2, S3, Diagram Tool",
        "Cron jobs, script automation",
        "WordPress, Tailwind"
    ],
    "Related Projects": [
        "AI Log Analyzer CLI, IDS project",
        "AI Log Analyzer, Summary Engine",
        "Portfolio, Hosting, MVP",
        "Monitor Tool, Email Alert",
        "mkcloudai.com"
    ],
    "Link to Notes / Code": [
        "[link to Week1Notes]",
        "[link to PromptTuning]",
        "[link to AWSSetupGuide]",
        "[link to CronJobNotes]",
        "[link to ThemeDocs]"
    ]
}

# Create folder if it doesn't exist
os.makedirs(folder, exist_ok=True)

# Create the DataFrame
df = pd.DataFrame(data)

# Save to Excel file
#excel_path = "/mnt/data/Freelance_Index.xlsx"
df.to_excel(file_path, index=False)

file_path
