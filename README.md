# Secure Data Encryption System

This is a simple web application built with Streamlit that lets you securely store and retrieve text using a passkey. It uses encryption to protect your data.

## What it Does

This application has a few main features:

* **Store:** You can type in some text and set a secret passkey. The app will then encrypt your text using a special method and store it. The passkey is also processed to make it more secure.
* **Retrieve:** If you have previously stored some encrypted text, you can paste it here and enter the passkey you used to save it. If you enter the correct passkey, the app will decrypt your text and show it to you.
* **Security:** The app uses strong encryption (Fernet) to make sure your stored text is protected. It also uses a way to scramble your passkey (hashing) so the original passkey isn't stored directly.
* **Login:** There's a simple login page with a master password. This is mainly there to reset the system if you try the wrong passkey too many times when retrieving data. The master password is `admin123` (but be careful, this is not very secure for real use!).

**Use the sidebar menu** on the left to navigate between the "Home", "Store", "Retrieve", and "Login" sections.
* **Home:** Just a welcome message.
* **Store:** Type your secret text and the passkey you want to use. Click "Save Securely". The app will show you the encrypted version of your text. Keep this encrypted text safe if you want to retrieve it later!
* **Retrieve:** Paste the encrypted text you saved earlier and enter the passkey you used. Click "Decrypt". If the passkey is correct, you'll see your original text. Be careful, if you enter the wrong passkey too many times, you might need to log in.
* **Login:** If you get locked out from retrieving, enter the master password (`admin123`) and click "Login" to reset the failed attempts.

# Huzaifa Khan Ghouri
# GIAIC #419013
