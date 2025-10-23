Caesar Cipher Web Application 🔒

A modern, interactive web-based tool for encrypting and decrypting text using the Caesar Cipher algorithm, complemented by a Python command-line version. Developed as part of the SkillCraft Technology internship program, this project showcases proficiency in front-end web development, Python scripting, and basic cryptography through intuitive interfaces.

🌐 Live Demo

Experience the web tool in action: Caesar Cipher Tool

📷 Preview



✨ Key Features





Real-Time Web Processing: Encrypts or decrypts text instantly on the web interface (e.g., "Hello There, General Kenobi" → "Vszzc Hvsfs, Usbsfoz Ysbcpw" with shift 66).



Command-Line Support: Offers a Python-based CLI for batch processing or offline use.



Customizable Shift Key: Supports any integer shift value (normalized to 0–25 using modulo 26).



Case Preservation: Retains uppercase and lowercase letters in both web and Python versions.



Non-Alphabetic Support: Preserves symbols, spaces, and numbers in their original positions.



Input Validation: Handles invalid inputs (e.g., non-numeric shift values, empty fields) with feedback in both interfaces.



Responsive Web Design: Optimized for desktop and mobile devices with a dark-themed UI.



Intuitive Interfaces: Features clear input fields, buttons on the web, and a CLI prompt in Python.

🛠️ Technologies Used





HTML5: Structures the web application’s layout and content.



CSS3: Delivers a responsive, dark-themed design for the web interface.



JavaScript: Implements the Caesar Cipher logic and real-time updates for the web tool.



Python: Powers the command-line version with robust scripting capabilities.

📖 Usage Instructions

Web Tool





Visit the live demo.



Enter a message in the text input (e.g., "Hello There, General Kenobi").



Specify a shift key (e.g., 66; large values are normalized to 0–25).



Click "Encrypt" or "Decrypt" to see the result (e.g., shift 66 encrypts to "Vszzc Hvsfs, Usbsfoz Ysbcpw").



Review the result; invalid inputs trigger error messages.

Python CLI





Clone the repository:

git clone https://github.com/KK-College/SCT_CS_01.git
cd SCT_CS_01



Ensure Python is installed (python3 --version).



Run the Python script:

python3 caesar_cipher.py



Follow the prompts to enter a message, shift key, and choose encrypt/decrypt options.





Example input: Message = "Hello There", Shift = 3, Mode = "encrypt" → Output: "Khoor Wkhuh".

🧩 Project Structure

SCT_CS_01/
├── index.html        # Main HTML file for the web application
├── styles.css        # CSS for styling and responsive web design
├── script.js         # JavaScript for Caesar Cipher logic and web interactivity
├── caesar_cipher.py  # Python script for the command-line version
└── README.md         # Project documentation

🚀 Getting Started Locally

Web Tool





Clone the Repository:

git clone https://github.com/KK-College/SCT_CS_01.git



Navigate to the Project Directory:

cd SCT_CS_01



Open the Application:





Open index.html in a web browser (e.g., Chrome, Firefox).



For a better experience, use a local server:

npx live-server

Python CLI





Follow the cloning steps above.



Install Python (if not already installed).



Run the script:

python3 caesar_cipher.py

🔐 Caesar Cipher Algorithm

The Caesar Cipher shifts each letter in the plaintext by a fixed number of positions in the alphabet:





Encryption: Shifts forward (e.g., shift 3: A → D; shift 66 % 26 = 14: H → V).



Decryption: Shifts backward to restore the original text.



Behavior:





Preserves case and non-alphabetic characters (e.g., spaces, punctuation).



Normalizes large shifts using modulo 26 (e.g., 66 → 14).

🛡️ Error Handling





Web Tool: Rejects non-numeric shifts and empty inputs with on-screen alerts.



Python CLI: Handles invalid inputs (e.g., non-integer shifts) with console error messages and prompts for retry.



Special Characters: Both versions maintain integrity of non-alphabetic characters.

📚 Learning Outcomes

This project demonstrates:





Implementation of the Caesar Cipher in JavaScript and Python.



Development of a responsive web interface and a CLI tool.



Effective input validation and error handling in multiple environments.



Deployment of a web application using GitHub Pages.



Cross-platform development with web and Python technologies.

📬 Contact

For inquiries or collaboration:





GitHub: KK-College



Email: [your-email@example.com] (replace with your email)

🙏 Acknowledgments

Developed under the SkillCraft Technology internship program. Thanks to the SkillCraft team for the opportunity to explore cryptography and multi-platform development.

📄 License

This project is licensed under the MIT License.
