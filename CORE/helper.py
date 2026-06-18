def loading_bar(progress, total, bar_length=30):
    percent = progress / total
    filled = int(bar_length * percent)
    bar = "#" * filled + "-" * (bar_length - filled)
    print(f"\r[{bar}] {percent*100:5.1f}%", end="")
