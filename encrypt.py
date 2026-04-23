import cv2
import os

def select_image():
    file_path = input("Enter the full path of the image: ").strip()
    if not os.path.exists(file_path):
        print("Error: File not found!")
        return None
    return file_path

def encrypt_image(image_path, msg, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Unable to load the image.")
        return None

    d = {chr(i): i for i in range(255)}
    n, m, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    encrypted_image_path = os.path.join(os.path.dirname(image_path), "encryptedImage.jpg")
    cv2.imwrite(encrypted_image_path, img)
    print(f"Encrypted image saved as: {encrypted_image_path}")

    password_file_path = os.path.join(os.path.dirname(image_path), "password.txt") #Save password
    with open(password_file_path, "w") as f:
        f.write(password)
    print(f"Password saved in: {password_file_path}")

    return encrypted_image_path

def main_encrypt():
    image_path = select_image()
    if not image_path:
        print("No image selected. Exiting...")
        return

    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    encrypted_image_path = encrypt_image(image_path, msg, password)
    if encrypted_image_path:
        print(f"Encryption completed. Check the file at {encrypted_image_path}")

main_encrypt()
