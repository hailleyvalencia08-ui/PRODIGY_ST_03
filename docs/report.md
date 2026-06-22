# Task‑03: Automated Login Test – Execution Report

## 🖥️ Test Environment
- **Browser:** Chrome (latest)
- **Framework:** Selenium + PyTest
- **OS:** Windows 11
- **Demo Site:** https://example.com/login

---

## 📊 Execution Results

| **TC ID** | **Scenario**            | **Expected Result**                          | **Actual Result**                          | **Status** |
|-----------|--------------------------|----------------------------------------------|--------------------------------------------|------------|
| TC01      | Valid Login              | User redirected to dashboard                 | Dashboard loaded successfully               | ✅ Pass |
| TC02      | Invalid Username         | Error message: "Invalid credentials"         | Error message displayed                     | ✅ Pass |
| TC03      | Invalid Password         | Error message: "Invalid credentials"         | Error message displayed                     | ✅ Pass |
| TC04      | Empty Username           | Error message: "Please enter username"       | Error message displayed                     | ✅ Pass |
| TC05      | Empty Password           | Error message: "Please enter password"       | Error message displayed                     | ✅ Pass |
| TC06      | Both Fields Empty        | Error message: "Please enter credentials"    | Error message displayed                     | ✅ Pass |
| TC07      | Case Sensitivity Check   | Error message: "Invalid credentials"         | Error message displayed                     | ✅ Pass |
| TC08      | Special Characters Check | Error message: "Invalid credentials"         | Error message displayed                     | ✅ Pass |

---

## 📸 Screenshot Evidence
- `screenshots/valid_login.png` → Successful login dashboard  
- `screenshots/invalid_login.png` → Error message for wrong credentials  
- `screenshots/empty_fields.png` → Error message for empty input  

---

## ✅ Conclusion
All login test cases executed successfully. The application correctly handled valid credentials and displayed appropriate error messages for invalid or empty inputs. The login functionality is **robust and reliable**.
