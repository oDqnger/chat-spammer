import keyboard
import time

def change_settings():
    message, exit_hotkey, delay, delay_all, how_long, amount_of_times = [],"", "", "", "", ""
    while True:
        try:
            count = int(input("How many unique messages would you like to spam? "))
            if count <= 0:
                print("\nPlease enter a number greater than 0!\n")
                continue

            for x in range(0, count):
                message.append(input("Enter the different types of messages you would like to spam: "))

            delay = float(input("How much delay would you like to have after a message has been spammed: "))

            if delay <= 0:
                print("\nERROR! Please enter a number greater than 0.\n")
                continue

            delay_all = float(input("How much delay would you like to have after *ALL* the messages have been sent: "))
            if delay_all < 0:
                print("\nERROR! Please enter a number greater than 0.\n")

            exit_hotkey = input("Enter a hotkey (can be anything as long as it has one letter) to stop the spammer when you need to: ")

            if len(exit_hotkey) != 1:
                print("\nERROR! Please enter a one character hotkey! Example: 'R' or '9'\n")
                continue

            try:
                how_long = float(input("OPTIONAL (to skip press enter): How long do you want to leave the spammer running for (seconds)? "))
                if how_long != "":
                    break

                if delay > how_long:
                    print("\nYou cannot have the timer longer than the delay!\n")
                    continue

            except:
                if how_long != "" and how_long <= 0:
                    print("\nERROR! Please type in a number (seconds)\n")
                    continue

            try:
                amount_of_times = int(input("OPTIONAL (to skip this press enter): How many times do you want the program to spam the message for: "))

                if amount_of_times <= 0:
                    print("\nERROR! The number must be greater than 0, not less than or equal to 0.")
                    continue

            except:
                if type(amount_of_times) == type("s") and amount_of_times != "":
                    print("\nERROR! Please enter a number!\n")
                    continue

        except:
            print("\nERROR! Please enter a number!\n")
            continue

        break

    return [message, delay, exit_hotkey, how_long, amount_of_times, delay_all]

def autoclicker(message, delay, delay_all):
    for x in message:
        try:
            keyboard.press(x)
        except:
            keyboard.write(x)

        time.sleep(delay)
        keyboard.press("enter")


    time.sleep(delay_all)

def main():

    message, delay, exit_hotkey, how_long, amount_of_times, delay_all = change_settings()
    while True:
        print("The spammer will begin in 5 seconds...")
        time.sleep(5)
        print("\nSpammer started!")

        start, end = time.time(), 0

        if amount_of_times == "":
            while True if how_long == "" else end - start <= how_long:
                if keyboard.is_pressed(exit_hotkey):
                    break

                autoclicker(message, delay, delay_all)
                end = time.time()
        else:
            for x in range(0, amount_of_times):
                if keyboard.is_pressed(exit_hotkey):
                    break

                autoclicker(message, delay, delay_all)

        print("\nSpammer ended.\n")

        while True:
            prompt = input("Would you like to change the settings, would you like to resume or would you want to quit the spammer? (c/r/q): ").lower()

            if prompt == "c":
                message, delay, exit_hotkey, how_long, amount_of_times, delay_all = change_settings()
                break
            elif prompt == "r":
                break
            elif prompt == "q":
                print("\nThanks for using the spammer!")
                exit()
            else:
                print("ERROR! Please type in either, 'c', 'r' or 'q.'")
                continue


if __name__ == "__main__":
    print("DISCLAIMER: I am not responsible for the way you use this software. This software may break yours, or other people's PC as this program has no limits\n")
    main()
