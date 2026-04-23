import cv2
import os

def decrypt_image(image_path, original_msg_length):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to load the image.")
        return None

    message = ""
    n, m, z = 0, 0, 0

    for i in range(original_msg_length):
        if n >= img.shape[0]:
            break
        char_value = img[n, m, z].item() 
        message += chr(char_value)

        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1

    return message


def main_decrypt():
    image_path = input("Enter the path to the encrypted image file: ").strip()
    if not os.path.exists(image_path):
        print("Error: Image file not found!")
        return

    password_file_path = input("Enter the path to the password file: ").strip()
    if not os.path.exists(password_file_path):
        print("Error: Password file not found!")
        return

    try:
        with open(password_file_path, "r", encoding="utf-8") as f:
            password = f.read().strip()
    except Exception as e:
        print(f"Error reading password file: {e}")
        return

    pas = input("Enter passcode for decryption: ").strip()
    if pas != password:
        print("ERROR: Incorrect passcode!")
        return

    try:
        original_msg_length = int(input("Enter the length of the original message: "))
    except ValueError:
        print("Error: Invalid input for message length.")
        return

    decrypted_message = decrypt_image(image_path, original_msg_length)
    if decrypted_message:
        print("\n Decrypted message:\n", decrypted_message)

        image_directory = os.path.dirname(image_path)
        output_file = os.path.join(image_directory, "decrypted_message.txt")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(decrypted_message)

        print(f"\n Decrypted message saved to '{output_file}'")
    else:
        print(" Decryption failed. Message might be corrupted.")

if __name__ == "__main__":
    main_decrypt()
