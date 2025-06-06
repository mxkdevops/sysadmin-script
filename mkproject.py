# mkproject.py
# -*- coding: utf-8 -*-
import os
import argparse
from datetime import datetime

TEMPLATE_README = """# 🚀 {project_name}

### 📌 Category
{category}

### 🎯 Objective
{objective}

### 🛠️ Tech Stack
{stack}

### 📁 Structure
- `/code/`: Scripts, Python files
- `/dashboard/`: HTML/visuals
- `/docs/`: Architecture, notes

### 🔧 How to Run
...

"""

TEMPLATE_BLOG = """# 📘 Project Blog – {project_name}

## 🧠 What is it?
{objective}

## 🛠️ Tools Used
{stack}

## 💡 Key Learnings
...

## 📸 Screenshots
...

"""

TEMPLATE_DESC = """### 📌 Project: {project_name}

**Category:** {category}  
**Objective:** {objective}  
**Start Date:** {start_date}  

**Stack:**  
{stack}
"""

def create_project(project_name, category, objective, stack):
    base_path = os.path.join(os.getcwd(), project_name)
    os.makedirs(base_path, exist_ok=True)
    os.makedirs(os.path.join(base_path, "code"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "dashboard"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "docs"), exist_ok=True)

    # Write README
    with open(os.path.join(base_path, "README.md"), "w", encoding="utf-8") as f:
        f.write(TEMPLATE_README.format(
            project_name=project_name,
            category=category,
            objective=objective,
            stack=stack
        ))

    # Write blog post
    with open(os.path.join(base_path, "blog_post.md"), "w", encoding="utf-8") as f:
        f.write(TEMPLATE_BLOG.format(
            project_name=project_name,
            objective=objective,
            stack=stack
        ))

    # Write project description
    with open(os.path.join(base_path, "description.md"), "w", encoding="utf-8") as f:
        f.write(TEMPLATE_DESC.format(
            project_name=project_name,
            category=category,
            objective=objective,
            start_date=datetime.today().strftime('%Y-%m-%d'),
            stack=stack
        ))

    # Write metadata
    with open(os.path.join(base_path, ".project_meta.json"), "w", encoding="utf-8") as f:
        f.write(f"""{{
  "project": "{project_name}",
  "category": "{category}",
  "objective": "{objective}",
  "stack": "{stack}",
  "created": "{datetime.today().isoformat()}"
}}""")

    print(f"\n✅ Project '{project_name}' scaffolded at {base_path}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🚀 Create a new AI/Cloud project folder with templates.")
    parser.add_argument("name", help="Project name (e.g., ai-cost-analyzer)")
    parser.add_argument("--category", default="AI | Cloud | Automation", help="Project category tags")
    parser.add_argument("--objective", default="TBD", help="Short summary of what this project does")
    parser.add_argument("--stack", default="Python, AWS, Bash, OpenAI, HTML", help="Technology stack")

    args = parser.parse_args()
    create_project(args.name, args.category, args.objective, args.stack)
