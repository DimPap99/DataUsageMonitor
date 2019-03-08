import time
import psutil
import easygui
import subprocess

def main():
    previous_data_used = 0
    while True:

        try:
            data_limit  = int(input("Data usage limit: "))
            break
        except ValueError:
            print("The given value must be a number")

    total_of_mb_used = 0

    while data_limit > total_of_mb_used:
        data_used_just_now = psutil.net_io_counters(pernic=False,nowrap=True).bytes_sent + psutil.net_io_counters(pernic=False,nowrap=True).bytes_recv

        if previous_data_used:
            print_mb(data_used_just_now - previous_data_used)
            total_of_mb_used += convert_to_mbyte(data_used_just_now - previous_data_used)

        previous_data_used = data_used_just_now
        time.sleep(0.3)

    window_pop_up("Megabyte data limit exceeded","Data Usage")
    error_code = subprocess.call("nmcli d disconnect wlp1s0",shell=True)
    if error_code == 0:
        print("Disconnected from the network")
    else:
        print("Something went wrong! You are probably not connected to the internet")


def convert_to_mbyte(value):
    return value / 1024. / 1024.


def print_mb(value):
    print("%0.1f" % convert_to_mbyte(value))

def window_pop_up(text,title):
    return  easygui.msgbox(text, title)

if __name__ == "__main__":

    main()






