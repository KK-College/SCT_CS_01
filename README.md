# Caesar Cipher Web Application 🔒

A modern, interactive web-based tool for encrypting and decrypting text using the Caesar Cipher algorithm, complemented by a Python command-line version. Developed as part of the SkillCraft Technology internship program, it showcases proficiency in front-end web development, Python scripting, and basic cryptography through intuitive interfaces.

## 🌐 Live Demo

Experience the web tool in action: [**Caesar Cipher Tool**](https://kk-college.github.io/SCT_CS_01/)

## ✨ Key Features

- **Real-time Processing**: Instant encryption and decryption directly in the browser.
- **Dual Interface**: Web-based UI for interactive use and Python CLI for batch processing.
- **Customizable Shift**: Supports any integer shift key (normalized modulo 26 for efficiency).
- **Preserves Formatting**: Maintains case sensitivity and leaves non-alphabetic characters unchanged.
- **Responsive Design**: Dark-themed, mobile-friendly interface for seamless experience across devices.
- **Input Validation**: Robust error handling to ensure valid inputs in both web and CLI modes.

## 🛠️ Technologies Used

| Technology | Description |
|------------|-------------|
| **HTML5** | Semantic structure and layout for the web application. |
| **CSS3** | Styling, animations, and responsive design with dark theme. |
| **JavaScript (ES6+)** | Core logic for real-time cipher operations and DOM manipulation. |
| **Python 3** | Command-line implementation with user-friendly prompts. |

## 📖 Usage Instructions

### Web Application
1. Open `index.html` in your web browser.
2. Enter the plaintext or ciphertext in the input field.
3. Specify the shift value (positive for encryption, negative for decryption).
4. Click **Encrypt** or **Decrypt** to process the text.
5. View the result in the output field.

### Python CLI
1. Run the script: `python caesar_cipher.py`.
2. Follow the prompts to enter your message, shift value, and mode (encrypt/decrypt).
3. The tool will output the processed text and allow for multiple operations.

