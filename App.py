import streamlit as st
import hashlib
from cryptography.fernet import Fernet

if "key" not in st.session_state:
    st.session_state.key = Fernet.generate_key()
    st.session_state.cipher = Fernet(st.session_state.key)

cipher = st.session_state.cipher

if "data_store" not in st.session_state:
    st.session_state.data_store = {}
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

def hash_key(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_data):
    return cipher.decrypt(encrypted_data.encode()).decode()

st.title("🔐 Secure Data Encryption System")
menu = ["Home", "Store", "Retrieve", "Login"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("🏠 Home")
    st.write("Simple in-memory secure app using passkey & encryption.")

elif choice == "Store":
    st.subheader("📥 Store Data")
    text = st.text_input("Enter your text:")
    passkey = st.text_input("Set a passkey:", type="password")

    if st.button("Save Securely"):
        if text and passkey:
            hashed = hash_key(passkey)
            encrypted = encrypt_data(text)
            st.session_state.data_store[encrypted] = hashed
            st.success(f"Data stored \n\n Encrypted Text : {encrypted}")
        else:
            st.error("⚠️ Please fill both fields.")

elif choice == "Retrieve":
    st.subheader("🔎 Retrieve Data")
    encrypted = st.text_input("Paste Encrypted Text:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        if st.session_state.failed_attempts >= 3:
            st.warning("🚫 Too many failed attempts, Please login again.")

        elif encrypted in st.session_state.data_store:
            hashed_input = hash_key(passkey)
            stored_hash = st.session_state.data_store[encrypted]

            if hashed_input == stored_hash:
                decrypted = decrypt_data(encrypted)
                st.success(f"🔓 Decrypted Data:\n\n{decrypted}")
                st.session_state.failed_attempts = 0
            else:
                st.session_state.failed_attempts += 1
                remaining = 3 - st.session_state.failed_attempts
                st.error(f"❌ Wrong passkey! Attempts left: {remaining}")
        
        else:
            st.error("❌ Encrypted text not found!")


elif choice == "Login":
    st.subheader("🔑 Login")
    master_pass = st.text_input("Enter Master Password:", type="password")
    st.write("password = admin123")

    if st.button("Login"):
        if master_pass == "admin123":
            st.session_state.failed_attempts = 0
            st.success("✅ Logged in! You can try retrieving again.")
        else:
            st.error("❌ Wrong password.")