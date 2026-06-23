import os

def loading_bar_animation(progress, total, bar_length=30):
    percent = progress / total
    filled = int(bar_length * percent)
    bar = "#" * filled + "-" * (bar_length - filled)

    # \r moves the cursor back to the start of the current line, return to column 0(begin of line) ,ex print(hello\rbo) ==  bollo
    # end="" prevents print from adding a newline (by defaut /n)
    
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

