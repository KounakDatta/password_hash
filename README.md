🔐 User Guide: Password Hashing and Verification with Bcrypt & Argon2
📘 Overview
This application allows you to:  

Hash passwords using Bcrypt and Argon2 algorithms.

Verify passwords against their respective hashes.

It's built with Streamlit, providing an interactive web interface for easy use.

🧑‍💻 How to Use the Application
Launch the Application:

Run the application using the command:

streamlit run app.py
Your default web browser will open the application interface.

Enter a Password to Hash:

In the "Password Input" section, enter the password you wish to hash.

Click the "Hash Password" button.

View Hashed Passwords:

After hashing, the application will display:

Bcrypt Hashed Password: The password hashed using the Bcrypt algorithm.

Argon2 Hashed Password: The password hashed using the Argon2 algorithm.

Verify the Password:

In the "Password Verification" section, enter the password you want to verify.

Click the "Verify Password" button.

The application will display verification results for both Bcrypt and Argon2:

Bcrypt Verification Result: Indicates whether the entered password matches the Bcrypt hash.

Argon2 Verification Result: Indicates whether the entered password matches the Argon2 hash.

🛡️ Security Considerations
Salting: Both Bcrypt and Argon2 automatically handle salting internally, enhancing security by ensuring that identical passwords result in different hashes.

Secure Input: The application uses Streamlit's text_input with type="password" to securely capture user passwords without displaying them on the screen.

Verification: The application verifies passwords without exposing the original password or hash.

📄 Requirements
Ensure you have the following Python packages installed:

streamlit

bcrypt

argon2-cffi

You can install them using:

bash
Copy
Edit
pip install streamlit bcrypt argon2-cffi
🧪 Example
Here's how the application works:

Input:

Password to hash: mysecretpassword

Password to verify: mysecretpassword

Output:

Bcrypt Hashed Password: $2b$12$...

Argon2 Hashed Password: $argon2id$v=19$...

Bcrypt Verification Result: True

Argon2 Verification Result: True

If you enter a different password in the verification step, the results will be False, indicating a mismatch


demo here:   https://passwordhash-m3scun7pszngannu3b6dqt.streamlit.app/
