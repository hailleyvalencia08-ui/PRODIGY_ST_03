# 🧪 Task‑03: Automated Login Test for a Web Application

## 📘 Objective
To design and implement an automated test suite that validates the login functionality of a web application using Selenium and PyTest.  
The goal is to ensure the system correctly handles valid and invalid login attempts, providing accurate feedback to users.

---

## 🔍 Scope of Testing
The test suite covers both **positive** and **negative** scenarios:

### ✅ Positive Case
- Valid username and valid password → Successful login, user redirected to dashboard/homepage.

### ❌ Negative Cases
- Invalid username with valid password → Error message displayed.
- Valid username with invalid password → Error message displayed.
- Empty username field → Prompt to enter username.
- Empty password field → Prompt to enter password.
- Both fields empty → Prompt to enter credentials.
- Case sensitivity check → Error message displayed for incorrect case.
- Special characters check → Error message displayed for invalid characters.

---

## 🛠️ Tools & Frameworks
- **Language:** Python  
- **Framework:** Selenium + PyTest  
- **Browser:** Chrome (latest)  
- **Operating System:** Windows 11  
- **Demo Site:** https://www.saucedemo.com/ 

---

## 📂 Repository Structure
