import os

LINE = "Someone hit reply-all to say 'Thanks!' to the whole company, and now 400 strangers are thanking each other in my inbox for an email I never read. Delete the reply-all button. Delete the building. I am going home and I am never checking email again."

OUTPUT = "/output/entry.txt"


def main():
    if not 1 <= len(LINE) <= 400:
        raise SystemExit("rant must be 1-400 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise SystemExit("rant must not be blank")
    if "\n" in LINE:
        raise SystemExit("rant must be a single block")
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
