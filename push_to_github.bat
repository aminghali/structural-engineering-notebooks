@echo off
echo.
echo =============================================
echo  GitHub Push Script
echo  Structural Engineering Notebooks
echo =============================================
echo.

echo Step 1: Checking git status...
git status

echo.
echo Step 2: Checking remote repository...
git remote -v

echo.
echo Step 3: Attempting to push to GitHub...
echo.
echo If authentication fails, you'll need to:
echo 1. Generate a Personal Access Token at: https://github.com/settings/tokens
echo 2. Use your GitHub username
echo 3. Use the token as password (not your GitHub password)
echo.

git push -u origin main

echo.
if %ERRORLEVEL% == 0 (
    echo ✅ SUCCESS: Your code has been pushed to GitHub!
    echo 🔗 Repository URL: https://github.com/aminghali/structural-engineering-notebooks
    echo.
    echo Your professional structural engineering project is now hosted on GitHub! 🎉
) else (
    echo ❌ FAILED: Push to GitHub failed.
    echo.
    echo Troubleshooting options:
    echo 1. Generate Personal Access Token: https://github.com/settings/tokens
    echo 2. Use GitHub CLI: gh auth login
    echo 3. Set up SSH keys: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
    echo.
    echo For manual push with token:
    echo git push https://YOUR_TOKEN@github.com/aminghali/structural-engineering-notebooks.git main
)

echo.
pause 