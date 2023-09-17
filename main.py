import keyboard
import time

def change_settings():
    exit_hotkey, delay, how_long = "", "", ""
    message = input("What's the message you would like to spam? ")
    while True:
        try:
            delay = float(input("How much delay would you like to have after a message has been spammed: "))
            exit_hotkey = input("Enter a hotkey (can be anything as long as it has one letter) to stop the spammer when you need to: ")

            if len(exit_hotkey) != 1:
                print("ERROR! Please enter a one character hotkey! Example: 'R' or '9'")
                continue

            try:
                how_long = float(input("OPTIONAL (to skip press enter): How long do you want to leave the spammer running for (seconds)? "))

                if delay > how_long:
                    print("You cannot have the timer longer than the delay!")
                    continue

            except:
                if how_long == "":
                    break
                else:
                    print("ERROR! Please type in a number (seconds)")
                    continue

        except:
            print("ERROR! Please enter a number!")
            continue

        break

    return [message, delay, exit_hotkey, how_long]

def main():

    message, delay, exit_hotkey, how_long = change_settings()

    while True:

        print("The spammer will begin in 5 seconds...")
        time.sleep(5)
        print("Spammer started!")

        start, end = time.time(), 0
        while True if how_long == "" else end - start <= how_long:
            if keyboard.is_pressed(exit_hotkey):
                print("Exiting!")
                break

            keyboard.write(message)
            keyboard.press("enter")

            time.sleep(delay)
            end = time.time()

        print("Spammer ended.\n")

        while True:
            prompt = input("Would you like to change the settings, would you like to resume or would you want to quit the spammer? (c/r/q): ").lower()

            if prompt == "c":
                message, delay, exit_hotkey, how_long = change_settings()
                break
            elif prompt == "r":
                break
            elif prompt == "q":
                print("Thanks for using the spammer!")
                exit()
            else:
                print("ERROR! Please type in either, 'c', 'r' or 'q.'")
                continue


if __name__ == "__main__":
    main()