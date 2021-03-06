try:
    with open(
            "website.html"
            , encoding="utf-8"
    ) as fp:
        contents = fp.read()
except FileNotFoundError as fnfe:
    print(f"ERROR| {fnfe}\nexiting...")
    exit(1)
except UnicodeDecodeError as ude:
    print(f"ERROR| {ude}\nexiting...")
    exit(2)
else:
    print(contents)
