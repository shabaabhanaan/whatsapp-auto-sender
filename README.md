# 📲 WhatsApp Personalized Message Sender (Python Automation)

Automate sending personalized WhatsApp messages to multiple contacts — either instantly or scheduled — using a simple and interactive Python script.

---

## 🚀 Features

- 🔄 **Send to Multiple Numbers** – Supports sending to multiple contacts at once.
- 💬 **Custom Message for Each Number** – Pair each phone number with a custom message.
- ⏰ **Schedule Messages** – Send now or set a time (24-hour format) for later delivery.
- 🌐 **WhatsApp Web Integration** – Uses `pywhatkit` to send messages through WhatsApp Web.
- 🔢 **Automatic Number Formatting** – Local numbers like `0771234567` are auto-converted to international format (`+94771234567`).

---

## 🛠️ How to Use

1. **Install Python and dependencies**:
   ```bash
   pip install pywhatkit
Run the script:

bash
Copy
Edit
python your_script_name.py
Follow the prompts:

Enter phone:message pairs like:

ruby
Copy
Edit
0771234567:Hello, 0759876543:Hi there, 0711111111:Good morning
Choose whether to send instantly (I) or schedule (S)

If scheduling, enter time in HH.MM or HH:MM (e.g., 21:30)

🧪 Example
Input:

ruby
Copy
Edit
0771234567:Hey!, 0759876543:Meeting at 5, 0788888888:Happy Birthday
Output:

css
Copy
Edit
Sending instantly to +94771234567...
Message sent to +94771234567.
...
Or for scheduled messages:

nginx
Copy
Edit
Scheduling message for +94771234567 at 21:30...
📋 Sample Log Format
yaml
Copy
Edit
Date: 02/07/2025
Time: 21:30
Phone Number: +94771234567
Message: Hello!
--------------------
⚠️ Notes
Make sure you are logged into WhatsApp Web on your default browser before running the script.

Message scheduling relies on your local system time.

Do not close the browser tab while the script is running.

💡 Tips
Add short delays between each message to avoid blocking.

Use responsibly — avoid spamming or violating WhatsApp’s terms.

🤝 Contribute
Feel free to fork this repo and submit pull requests with improvements (like .csv support, GUI version, or logs to file).

📌 Author
Shabaab Hanaan
🔗 LinkedIn
💻 GitHub

Happy Automating! 💬🚀

![what](https://github.com/user-attachments/assets/a9e8e3ca-3c51-4b65-bb76-06cf93f468a7)

