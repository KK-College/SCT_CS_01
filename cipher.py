def caesar_cipher(text: str, shift: int, mode: str) -> str:
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.

    Args:
        text (str): Input string to process.
        shift (int): Number of positions to shift letters (0-25).
        mode (str): 'encrypt' or 'decrypt'.

    Returns:
        str: Processed (encrypted or decrypted) string.

    Raises:
        ValueError: If mode is invalid or shift is out of range.
    """
    if mode not in ['encrypt', 'decrypt']:
        raise ValueError("Mode must be 'encrypt' or 'decrypt'")
    
    # Normalize shift to 0-25 range
    shift = shift % 26
    if mode == 'decrypt':
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_pos = (ord(char) - start + shift) % 26
            result.append(chr(start + shifted_pos))
        else:
            result.append(char)
    
    return ''.join(result)

def get_valid_shift() -> int:
    """Prompts user for a valid shift value."""
    while True:
        try:
            shift = int(input("Enter shift key (1-25): "))
            if 1 <= shift <= 25:
                return shift
            print("Shift must be between 1 and 25.")
        except ValueError:
            print("Please enter a valid number.")

def get_valid_mode() -> str:
    """Prompts user for a valid mode (encrypt/decrypt)."""
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
        if choice in ['e', 'd']:
            return 'encrypt' if choice == 'e' else 'decrypt'
        print("Invalid choice! Please enter 'e' or 'd'.")

def get_valid_message() -> str:
    """Prompts user for a non-empty message."""
    while True:
        message = input("Enter your message: ").strip()
        if message:
            return message
        print("Message cannot be empty.")

def main():
    """Main function to run the Caesar Cipher program."""
    print("Caesar Cipher Program")
    print("=====================")

    while True:
        try:
            mode = get_valid_mode()
            message = get_valid_message()
            shift = get_valid_shift()
            
            result = caesar_cipher(message, shift, mode)
            action = "Encrypted" if mode == 'encrypt' else "Decrypted"
            print(f"\n{action} Message: {result}\n")

            again = input("Do you want to go again? (yes/no): ").lower()
            if again != 'yes':
                print("Thank you for using the KK's Caesar Cipher Program!")
                break

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()