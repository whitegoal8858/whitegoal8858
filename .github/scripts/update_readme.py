import os
import re
import urllib.request
import json

USERNAME = "whitegoal8858"
EXCLUDE = {"whitegoal8858", "whitegoal8858.github.io"}

def get_repos():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("METRICS_TOKEN")
    headers = {"User-Agent": "Mozilla/5.0"}
    if token:
        headers["Authorization"] = f"token {token}"
    
    url = f"https://api.github.com/users/{USERNAME}/repos?sort=updated&per_page=100"
    req = urllib.request.Request(url, headers=headers)
    
    with urllib.request.urlopen(req) as resp:
        repos = json.loads(resp.read().decode("utf-8"))
    
    filtered = [r for r in repos if r["name"] not in EXCLUDE and not r.get("fork", False)]
    return filtered

def format_project_card(r):
    name = r["name"]
    url = r["html_url"]
    desc = r.get("description")
    if not desc or desc.strip() == "":
        desc = "Modern software application & engineering codebase."
    
    lang = r.get("language") or "Full-Stack"
    stars = r.get("stargazers_count", 0)
    forks = r.get("forks_count", 0)
    
    star_badge = f"⭐ {stars}" if stars > 0 else ""
    fork_badge = f"🍴 {forks}" if forks > 0 else ""
    meta_badges = " • ".join(filter(None, [f"`{lang}`", star_badge, fork_badge]))
    
    return f"""#### 🚀 [{name}]({url})
> {desc}
- **Tech / Meta**: {meta_badges}
- 🔗 **View Repository**: [{url}]({url})
"""

def update_readme():
    repos = get_repos()
    top_repos = repos[:8]
    
    project_sections = [format_project_card(r) for r in top_repos]
    content = "\n".join(project_sections)
    
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        readme_path = os.path.join(os.path.dirname(__file__), "..", "..", "README.md")
    
    with open(readme_path, "r", encoding="utf-8") as f:
        readme = f.read()
    
    pattern = r"(<!-- AUTOMATED-PROJECTS-LIST:START -->)(.*?)(<!-- AUTOMATED-PROJECTS-LIST:END -->)"
    replacement = f"\\1\n\n{content}\n\\3"
    
    new_readme = re.sub(pattern, replacement, readme, flags=re.DOTALL)
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_readme)
    
    print(f"Successfully auto-synced {len(top_repos)} repositories into README.md")

if __name__ == "__main__":
    update_readme()
