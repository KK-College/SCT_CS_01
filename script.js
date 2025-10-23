document.addEventListener('DOMContentLoaded', () => {
    // Get references to all the HTML elements
    const inputText = document.getElementById('inputText');
    const shiftKey = document.getElementById('shiftKey');
    const encryptBtn = document.getElementById('encryptBtn');
    const decryptBtn = document.getElementById('decryptBtn');
    const resultText = document.getElementById('resultText');

    function processText(mode) {
        const text = inputText.value;
        let shift = parseInt(shiftKey.value);

        // For decryption, the shift is inverted
        if (mode === 'decrypt') {
            shift = -shift;
        }

        const result = text.split('').map(char => {
            if (char.match(/[a-z]/i)) { // Check if it's a letter (case-insensitive)
                const code = char.charCodeAt(0);
                let start;

                // Handle uppercase and lowercase letters separately
                if (code >= 65 && code <= 90) { // Uppercase (A-Z)
                    start = 65;
                } else if (code >= 97 && code <= 122) { // Lowercase (a-z)
                    start = 97;
                }
                
                // The core formula for shifting and wrapping
                let shiftedCode = (code - start + shift) % 26;
                if (shiftedCode < 0) {
                    shiftedCode += 26; // Ensure result is positive for decryption
                }
                
                return String.fromCharCode(start + shiftedCode);
            }
            return char; // Return non-alphabetic characters as they are
        }).join('');

        resultText.textContent = result;
    }

    // Add click event listeners to the buttons
    encryptBtn.addEventListener('click', () => processText('encrypt'));
    decryptBtn.addEventListener('click', () => processText('decrypt'));
});