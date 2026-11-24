import os

# One-Star Review of Something Essential: sleep.
#
# The grievance is the one everyone recognises but never files:
# sleep takes a full eight hours every night and still delivers
# you to work tired. Framed deadpan as a consumer complaint
# against a service that cannot be fixed, with the sting in the
# last three words: no refund policy. "Charges" and "delivers"
# keep the review in the voice of a customer filing a complaint
# about a paid service. No exclamation marks, no wink, one joke,
# one line.
REVIEW = "Sleep charges eight hours a night and still delivers me to work tired. No refund policy."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)
    # Guard the gate: 1-160 chars, single line, not only whitespace.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if not 1 <= len(written) <= 160 or not written.strip() or "\n" in written:
        raise ValueError("entry.txt must be a single line of 1-160 chars, got %r" % written)


if __name__ == "__main__":
    main()
