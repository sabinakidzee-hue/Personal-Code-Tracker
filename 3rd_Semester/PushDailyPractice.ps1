# PushDailyPractice.ps1
# Auto-add, commit, and push new Python practice files to GitHub

# Navigate to repo (optional if script is run from repo)
cd "C:\Users\sabin\OneDrive\Documents\Personal-Code-Tracker"

# Pull latest changes from GitHub to avoid conflicts
git pull origin main

# Stage all new/modified Python practice files
git add 3rd_Semester/Python_Practice/*

# Commit with today's date
$today = Get-Date -Format "yyyy-MM-dd"
git commit -m "Add Python practice file for $today"

# Push to GitHub
git push origin main

Write-Host "`n✅ All Python practice files pushed successfully!"
