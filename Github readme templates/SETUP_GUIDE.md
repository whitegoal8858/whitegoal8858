# 🚀 How to Enable 100% Match Live GitHub Metrics Dashboard

Aapke provide kiye gaye screenshot wala design **`lowlighter/metrics`** ka official infographic dashboard hai. Ye directly GitHub Actions ke through aapke profile repository me run hota hai aur **har 12 ghante me live data fetch karke `github-metrics.svg` generate karta hai**.

---

## 📋 Quick Setup Steps (Only 2 Minutes)

### Step 1: Create a Personal Access Token (PAT)
1. GitHub par login karein aur **[GitHub Settings > Developer Settings > Tokens (classic)](https://github.com/settings/tokens)** par jayein.
2. **Generate new token (classic)** par click karein.
3. Note me likhein: `METRICS_TOKEN`.
4. Expiration choose karein: `No expiration` (ya apni preference ke hisaab se).
5. Niche diye gaye scopes par checkmark (tick) lagayein:
   - ✅ `repo` (Full control of private repositories - agar private commits bhi show karni hain)
   - ✅ `read:org` (Read org data)
   - ✅ `read:user` (Read all user profile data)
   - ✅ `read:packages`
   - ✅ `gist`
6. **Generate token** button par click karein aur generated token ko copy kar lein (`ghp_...`).

---

### Step 2: Add Secret to your Profile Repository
1. Apne profile repository **`https://github.com/sajalsrivastava/sajalsrivastava`** par jayein.
2. Repository ke **Settings** tab par click karein.
3. Left sidebar me **Secrets and variables** > **Actions** par click karein.
4. **New repository secret** par click karein:
   - **Name**: `METRICS_TOKEN`
   - **Secret**: Copy kiya hua token (`ghp_...`) paste karein.
5. **Add secret** par click karein.

---

### Step 3: Enable Workflow Permissions
1. Usi repository ke **Settings** > **Actions** > **General** me jayein.
2. Niche scroll karein aur **Workflow permissions** me **Read and write permissions** ko select karke **Save** kar dein. *(Ye permission action ko `github-metrics.svg` commit karne ke liye zaroori hoti hai).*

---

### Step 4: Run the Action Manually (First Time)
1. Apne repository ke **Actions** tab par jayein.
2. Left side me **Metrics** workflow par click karein.
3. Right side me **Run workflow** dropdown par click karke **Run workflow** press karein.
4. 1 se 2 minute me action complete ho jayega aur repository root me **`github-metrics.svg`** generate ho jayega.
5. Aapka README turant exact screenshot jaise visually stunning dark dashboard me live ho jayega!

---

## 📁 Files Included in this Folder:
- **`README.md`**: Complete, unique GitHub Profile README tailored for ERP, Web & Mobile Development.
- **`.github/workflows/metrics.yml`**: Pre-configured GitHub Action workflow with all exact plugins from the screenshot (PageSpeed, Isometric 3D Calendar, Coding Habits, Language Activity, Mastered Topics, and Projects).
