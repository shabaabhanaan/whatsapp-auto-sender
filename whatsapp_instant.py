import pywhatkit as kit
import datetime

def format_number(num):
    num = num.strip()
    # If already starts with +, return as is
    if num.startswith("+"):
        return num
    # If starts with 0 and 10 digits, replace 0 with +94
    if len(num) == 10 and num.startswith("0"):
        return "+94" + num[1:]
    return num

def parse_time(time_str):
    # Allow formats like "21.46" or "21:46"
    if "." in time_str:
        parts = time_str.split(".")
    elif ":" in time_str:
        parts = time_str.split(":")
    else:
        parts = [time_str, "0"]

    if len(parts) != 2:
        raise ValueError("Time must be in HH.MM or HH:MM format")

    hour = int(parts[0])
    minute = int(parts[1])

    if not (0 <= hour <= 23) or not (0 <= minute <= 59):
        raise ValueError("Hour must be 0-23 and minute 0-59")

    return hour, minute

def main():
    print("WhatsApp Message Sender")

    raw_phone = input("Enter phone number (e.g. 0912234567 or +94712234567): ").strip()
    phone = format_number(raw_phone)

    if not phone.startswith("+94") or len(phone) != 12:
        print("Invalid phone number format. Please enter 10 digits starting with 0 or full number with +94.")
        return

    message = input("Enter your message: ").strip()
    if not message:
        print("Message cannot be empty.")
        return

    choice = input("Send message instantly or schedule for later? [I/S]: ").strip().upper()

    if choice == "I":
        print(f"Sending message instantly to {phone}...")
        kit.sendwhatmsg_instantly(phone, message, wait_time=10, tab_close=True)
        print("Message sent.")
    elif choice == "S":
        try:
            time_input = input("Enter time to send (HH.MM or HH:MM, 24-hour format): ").strip()
            hour, minute = parse_time(time_input)

            now = datetime.datetime.now()
            scheduled_time = datetime.datetime(now.year, now.month, now.day, hour, minute)
            if scheduled_time < now:
                scheduled_time += datetime.timedelta(days=1)

            print(f"Scheduling message for {scheduled_time.strftime('%Y-%m-%d %H:%M')} to {phone}...")
            kit.sendwhatmsg(phone, message, scheduled_time.hour, scheduled_time.minute, wait_time=15, tab_close=True)
            print("Message scheduled.")
        except ValueError as e:
            print(f"Invalid time entered: {e}")
    else:
        print("Invalid choice. Please select 'I' or 'S'.")

if __name__ == "__main__":
    main()
