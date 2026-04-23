# Image Steganography with Encryption (Python)

## Overview
This project implements secure data hiding in images by combining encryption and steganography.

The secret message is first encrypted and then embedded into an image, ensuring both confidentiality and stealth during transmission.

---

## How It Works

1. The secret message is encrypted using a passcode  
2. Encrypted data is embedded into an image (pixel-level encoding)  
3. The image is shared securely  
4. The receiver extracts and decrypts the hidden message  

---

## Project Structure

- encrypt.py → Encrypts the secret message and embeds it into the image  
- decrypt.py → Extracts and decrypts the hidden message  
- steganography_basic.py → Basic implementation of image steganography  

---

## Tech Stack

- Python  
- OpenCV  
- NumPy  
- Pillow  

---

## How to Run

1. Install dependencies:
pip install opencv-python numpy pillow

2. Run encryption:
python encrypt.py

3. Hide message in image:
python steganography_basic.py

4. Decrypt message:
python decrypt.py

---

## Key Features

- Dual-layer security (encryption + steganography)  
- Image-based hidden communication  
- Pixel-level data embedding  
- Password-protected decryption  

---

## Use Cases

- Secure communication  
- Cybersecurity applications  
- Data protection  
- Confidential information sharing  

---

## Future Improvements

- Support for video and audio steganography  
- AI-based detection resistance  
- Real-time secure messaging  
- Cloud-based encrypted communication  

---

## Author

Developed as part of internship work at Edunet Foundation in collaboration with IBM SkillsBuild.
