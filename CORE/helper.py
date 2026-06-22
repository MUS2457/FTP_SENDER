import os

def loading_bar_animation(progress, total, bar_length=30):
    percent = progress / total
    filled = int(bar_length * percent)
    bar = "#" * filled + "-" * (bar_length - filled)

    # \r moves the cursor back to the start of the current line
    # It does NOT erase the line ,return to column 0(begin of line)
    # ex print("hello\rbye") bye overwrites hel output byelo
    # end="" prevents print() from adding a newline (\n)
    # without end="", print() would move to the next line, breaking the overwrite effect
    print(f"\r[{bar}] {percent*100:5.1f}%", end="")


def folder_scanner(folder_path):
    files = []
    
    try :
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)

            if os.path.isfile(item_path) :
                files.append(item_path)
            
            elif os.path.isdir(item_path) :
                sub_files = folder_scanner(item_path)
                files.extend(sub_files)

    except OSError :
        pass

    return files

