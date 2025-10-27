@echo off

set /p VERSION=<../VERSION

for /f "tokens=* delims= " %%a in ("%VERSION%") do set VERSION=%%a

poetry version %VERSION%

for /f %%i in ('git merge-base HEAD origin/main') do set BASE=%%i

git reset %BASE%

git add -A

git commit -m "version = \"v%VERSION%\""

git push -f origin main

git tag v%VERSION%

git push origin v%VERSION%