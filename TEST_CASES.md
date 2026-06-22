# Task‑03: Automated Login Test – Detailed Test Cases

## 📄 Objective
To validate the login functionality of a demo web application by covering both positive and negative scenarios. Each test case includes ID, description, steps, expected result, actual result, and status.

---

### ✅ Positive Test Case

**TC01 – Valid Login**
- **Description:** Verify that a user can successfully log in with valid credentials.  
- **Precondition:** User account exists with correct username and password.  
- **Steps:**  
  1. Navigate to the login page.  
  2. Enter a valid username.  
  3. Enter the correct password.  
  4. Click the **Login** button.  
- **Expected Result:** User is redirected to the dashboard/homepage. A welcome message or user profile is displayed.  
- **Actual Result:** [Execution Result]  
- **Status:** Pass/Fail  

---

### ❌ Negative Test Cases

**TC02 – Invalid Username**
- **Description:** Verify login fails when the username is incorrect.  
- **Steps:**  
  1. Navigate to the login page.  
  2. Enter an invalid username.  
  3. Enter a valid password.  
  4. Click the **Login** button.  
- **Expected Result:** Error message displayed: *“Invalid credentials”*. User remains on login page.  
- **Actual Result:** [Execution Result]  
- **Status:** Pass/Fail  

---

**TC03 – Invalid Password**
- **Description:** Verify login fails when the password is incorrect.  
- **Steps:**  
  1. Navigate to the login page.  
  2. Enter a valid username.  
  3. Enter an invalid password.  
  4. Click the **Login** button.  
- **Expected Result:** Error message displayed: *“Invalid credentials”*. User remains on login page.  
- **Actual Result:** [Execution Result]  
- **Status:** Pass/Fail  

---

**TC04 – Empty Username**
- **Description:** Verify login fails when the username field is left blank.  
- **Steps:**  
  1. Navigate to the login page.  
  2. Leave the username field empty.  
  3. Enter a valid password.  
  4. Click the **Login** button.  
- **Expected Result:** Error message displayed: *“Please enter username”*.  
- **Actual Result:** [Execution Result]  
- **Status:** Pass/Fail  

---

**TC05 – Empty Password**
- **Description:** Verify login fails when the password field is left blank.  
- **Steps:**  
  1. Navigate to the login page.  
  2. Enter a valid username.  
  3. Leave the password field empty.  
  4. Click the **Login** button.  
- **Expected Result:** Error message displayed: *“Please enter password”*.  
- **Actual Result:** [Execution Result]  
- **Status:** Pass/Fail  

---

**TC06 – Both Fields Empty**
- **Description:** Verify login fails when both username and password fields are left blank.  
- **Steps:**  
  1. Navigate to the login page.  
  2. Leave both fields empty.  
  3. Click the **Login** button.  
- **Expected Result:** Error message displayed: *“Please enter credentials”*.  
- **Actual Result:** [Execution Result]  
- **Status:** Pass/Fail  

---

**TC07 – Case Sensitivity Check**
- **Description:** Verify login fails when username/password case does not match stored credentials.  
- **Steps:**  
  1. Navigate to the login page.  
  2. Enter username in uppercase/lowercase incorrectly.  
  3. Enter password with incorrect case.  
  4. Click the **Login** button.  
- **Expected Result:** Error message displayed: *“Invalid credentials”*.  
- **Actual Result:** [Execution Result]  
- **Status:** Pass/Fail  

---

**TC08 – Special Characters Check**
- **Description:** Verify login fails when special characters are entered in username/password fields.  
- **Steps:**  
  1. Navigate to the login page.  
  2. Enter username with special characters (e.g., `user!@#`).  
  3. Enter password with special characters not allowed.  
  4. Click the **Login** button.  
- **Expected Result:** Error message displayed: *“Invalid credentials”*.  
- **Actual Result:** [Execution Result]  
- **Status:** Pass/Fail  

---

