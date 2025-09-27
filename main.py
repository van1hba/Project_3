import customtkinter as ctk
from tkinter import messagebox
import pyperclip

CIPHERS = {
    "AES": "aes_cipher",
    "DES": "des_cipher",
    "Triple DES": "triple_des_cipher",
    "Fernet": "fernet_cipher",
    "Blowfish": "blowfish_cipher",
    "RC4": "rc4_cipher",
    "ChaCha20": "chacha20_cipher"
}

def load_cipher_module(name):
    return __import__(f'encryption.{name}', fromlist=['encrypt', 'decrypt'])

def encrypt_decrypt():
    algo = algo_combo.get()
    password = password_entry.get()
    text = input_box.get("0.0", "end").strip()

    if not text or not password or not algo:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    try:
        module = load_cipher_module(CIPHERS[algo])
        try:
            result = module.decrypt(text, password)
            result_label.configure(text="✅ Decrypted")
        except:
            result = module.encrypt(text, password)
            result_label.configure(text="🔐 Encrypted")
        output_box.delete("0.0", "end")
        output_box.insert("0.0", result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def copy_result():
    result = output_box.get("0.0", "end").strip()
    if result:
        pyperclip.copy(result)
        messagebox.showinfo("Copied", "Output copied to clipboard.")

# --- GUI Setup ---
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.title("🔐 Multi Encryption Tool")
root.geometry("700x600")

ctk.CTkLabel(root, text="Multi Encryption Tool", font=("Arial", 20, "bold")).pack(pady=15)
algo_combo = ctk.CTkComboBox(root, values=list(CIPHERS.keys()), width=300)
algo_combo.set("AES")
algo_combo.pack(pady=10)

password_entry = ctk.CTkEntry(root, placeholder_text="Enter password / key", show="*", width=400)
password_entry.pack(pady=10)

input_box = ctk.CTkTextbox(root, width=600, height=100)
input_box.pack(pady=(10, 5))
input_box.insert("0.0", "Enter your text here...")

ctk.CTkButton(root, text="🔁 Encrypt / Decrypt", command=encrypt_decrypt).pack(pady=10)

result_label = ctk.CTkLabel(root, text="Result will appear below 👇", font=("Arial", 12, "italic"))
result_label.pack()

output_box = ctk.CTkTextbox(root, width=600, height=100)
output_box.pack(pady=(5, 10))

ctk.CTkButton(root, text="📋 Copy to Clipboard", command=copy_result).pack()
ctk.CTkLabel(root, text="Made by Abhinav & Arushita", font=("Arial", 10)).pack(pady=10)

root.mainloop()
