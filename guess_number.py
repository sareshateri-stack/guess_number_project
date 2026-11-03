import random

# تنظیمات بازی
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 5


def play_game():
    """اجرای یک دور از بازی حدس اعداد."""
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts_used = 0
    won = False

    print("\n==============================")
    print("        بازی حدس اعداد")
    print("==============================")
    print("یک عدد بین 1 تا 100 انتخاب شده است.")
    print("شما 5 فرصت برای حدس زدن دارید.\n")

    while attempts_used < MAX_ATTEMPTS:
        print("------------------------------")
        print(f"تلاش {attempts_used + 1} از {MAX_ATTEMPTS}")
        print(f"جان باقی‌مانده: {MAX_ATTEMPTS - attempts_used}")

        user_input = input("حدس خود را وارد کنید: ").strip()

        # اعتبارسنجی: ورودی باید عدد صحیح باشد.
        try:
            guess = int(user_input)
        except ValueError:
            print("خطا! لطفاً فقط عدد صحیح وارد کنید.")
            continue

        # ورودی خارج از بازه، فرصت را کم نمی‌کند.
        if not MIN_NUMBER <= guess <= MAX_NUMBER:
            print("عدد باید بین 1 تا 100 باشد.")
            continue

        # فقط حدس معتبر، یک فرصت مصرف می‌کند.
        attempts_used += 1

        if guess == secret_number:
            print("\nآفرین! شما برنده شدید.")
            print(f"عدد مخفی: {secret_number}")
            print(f"تعداد تلاش‌های شما: {attempts_used}")

            ranks = {
                1: "نمونه‌ای!",
                2: "بسیار خوبی!",
                3: "خوب!",
                4: "قبول!",
                5: "با شانس بردی!"
            }
            print(f"رتبه شما: {ranks[attempts_used]}")

            won = True
            break

        # محاسبه فاصله حدس تا عدد مخفی
        difference = abs(guess - secret_number)

        # راهنمای جهت حدس
        if guess < secret_number:
            direction_message = "عدد مخفی بزرگ‌تر است؛ بزرگ‌تر وارد کن!"
        else:
            direction_message = "عدد مخفی کوچک‌تر است؛ کوچک‌تر وارد کن!"

        # راهنمای میزان نزدیکی
        if difference <= 5:
            distance_message = "خیلی نزدیکی!"
        elif difference <= 15:
            distance_message = "نزدیکی، ولی هنوز فاصله داری!"
        else:
            distance_message = "خیلی دوری!"

        print(direction_message)
        print(distance_message)
        print(f"فرصت‌های باقی‌مانده: {MAX_ATTEMPTS - attempts_used}")

    if not won:
        print("\nمتأسفانه فرصت‌های شما تمام شد!")
        print(f"عدد مخفی {secret_number} بود.")
        print("شما این دور را باختید.")


def play_again():
    """پرسیدن اینکه کاربر می‌خواهد دوباره بازی کند یا نه."""
    while True:
        answer = input(
            "\nآیا می‌خواهید دوباره بازی کنید؟ (بله/خیر): "
        ).strip().lower()

        if answer in ["بله", "بلی", "آره", "اره", "yes", "y"]:
            return True
        elif answer in ["خیر", "نه", "no", "n"]:
            return False
        else:
            print("لطفاً فقط بله یا خیر وارد کنید.")


def main():
    """تابع اصلی برنامه."""
    print("به بازی حدس اعداد خوش آمدید!")

    while True:
        play_game()

        if not play_again():
            print("\nممنون از بازی شما!")
            print("برنامه به پایان رسید.")
            break


if __name__ == "__main__":
    main()
