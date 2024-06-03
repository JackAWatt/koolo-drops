import os
import time
import winsound

hr_sound_played = 0
hr_sound_location = "C:\\Users\\9t32um\\Documents\\koolo\\koolo_6_03\\highrune.wav"
hr = ["Vex", "Ohm", "Lo", "Sur", "Ber", "Jah", "Cham", "Zod"]
mr = ["Um", "Mal", "Ist", "gul"]


def x_in_y(x,y):
    for yy in y:
        if x in y:
            return true
os.system('color')
d = "C:\\Users\\9t32um\\Documents\\koolo\\koolo_6_03\\logs"
while 1:
    hr_count = 0
    os.system('cls')
    print("\n")
    def all_files_under(path):
        for cur_path, dirnames, filenames in os.walk(path):
            for filename in filenames:
                yield os.path.join(cur_path, filename)


    latest_file = max(all_files_under(d), key=os.path.getmtime)


    f = open(latest_file, "r")

            
    f = f.read()
    f = f.split("\n")
    out = []
    for ff in f:
        if "Normal" in ff or "Unique" in ff:
            if "Super" not in ff and "Rejuv" not in ff and "Flawless" not in ff:
                if "DEBUG" not in ff:
                    ff = ff.replace('level=INFO', '')
                    ff = ff.replace('level=DEBUG', '')
                    ff = ff.replace('msg=', '')
                    ff = ff.replace('"', '')
                    out = out + [ff]

    for o in out:
        if "Key" in o:
            print('\x1b[6;30;42m'+o+'\x1b[0m')
        else:
            if "Normal" in o:
                if x_in_y(o,mr):
                    print('\x1b[0;37;40m'+o+'\x1b[0m')
                elif x_in_y(o,hr):
                    print('\x1b[1;37;45m'+o+'\x1b[0m')
                    hr_count = hr_count + 1
                else:
                    print(o)

    if hr_sound_played < hr_count:
        winsound.PlaySound(hr_sound_location, winsound.SND_FILENAME |
                           winsound.SND_ASYNC)
        hr_sound_played = hr_count
    print("\nwill update every 60 seconds")
    time.sleep(60)
