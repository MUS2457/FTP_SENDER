def loading_bar(progress, total, bar_length=30):
    percent = progress / total
    filled = int(bar_length * percent)
    bar = "#" * filled + "-" * (bar_length - filled)

    # \r moves the cursor back to the start of the current line
    # It does NOT erase the line ,return to column 0(begin of line)
    # ex print("hello\rbye") bye overwrites hel output byelo
    # end="" prevents print() from adding a newline (\n)
    # without end="", print() would move to the next line, breaking the overwrite effect
    print(f"\r[{bar}] {percent*100:5.1f}%", end="")
