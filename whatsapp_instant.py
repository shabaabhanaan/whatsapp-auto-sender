import pywhatkit as kit
import datetime
import time

def format_number(num):
    num = num.strip()
    if num.startswith("+"):
        return num
    if len(num) == 10 and num.startswith("0"):
        return "+94" + num[1:]
    return num

def parse_time(time_str):
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
    print("WhatsApp Personalized Message Sender")

    raw_input = input("Enter phone:message pairs separated by commas\n(e.g. 0771234567:Hello, 0759876543:Hi there):\n")
    
    # Parse input into list of tuples (phone, message)
    pairs = []
    for pair in raw_input.split(","):
        if ":" not in pair:
            print(f"Skipping invalid input: {pair.strip()}")
            continue
        phone, msg = pair.split(":", 1)
        phone = format_number(phone.strip())
        msg = msg.strip()
        if not phone.startswith("+94") or len(phone) != 12:
            print(f"Invalid phone number skipped: {phone}")
            continue
        if not msg:
            print(f"Empty message for {phone}, skipped.")
            continue
        pairs.append( (phone, msg) )

    if not pairs:
        print("No valid phone:message pairs entered. Exiting.")
        return

    choice = input("Send instantly or schedule? [I/S]: ").strip().upper()

    if choice == "I":
        for phone, msg in pairs:
            print(f"Sending instantly to {phone}...")
            kit.sendwhatmsg_instantly(phone, msg, wait_time=10, tab_close=True)
            print(f"Message sent to {phone}.")
            time.sleep(5)
    elif choice == "S":
        try:
            time_input = input("Enter time to send (HH.MM or HH:MM, 24-hour format): ").strip()
            hour, minute = parse_time(time_input)
            now = datetime.datetime.now()
            scheduled_time = datetime.datetime(now.year, now.month, now.day, hour, minute)
            if scheduled_time < now:
                scheduled_time += datetime.timedelta(days=1)

            for i, (phone, msg) in enumerate(pairs):
                # Schedule each message a minute apart
                send_time = scheduled_time + datetime.timedelta(minutes=i)
                print(f"Scheduling message for {phone} at {send_time.strftime('%H:%M')}...")
                kit.sendwhatmsg(phone, msg, send_time.hour, send_time.minute, wait_time=15, tab_close=True)
                time.sleep(10)
            print("All messages scheduled.")
        except ValueError as e:
            print(f"Invalid time entered: {e}")
    else:
        print("Invalid choice. Please enter 'I' or 'S'.")

if __name__ == "__main__":
    main()
