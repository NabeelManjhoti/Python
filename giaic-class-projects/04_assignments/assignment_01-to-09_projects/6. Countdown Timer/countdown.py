import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"\r⏳ Time Left: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1

    print("\n🚀 Time's up!")


try:
    user_time = int(input("\nEnter countdown time in seconds: "))
    countdown_timer(user_time)
except ValueError:
    print("Invalid input! Please enter a valid number.")