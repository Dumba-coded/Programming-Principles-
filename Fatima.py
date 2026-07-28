RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'

print(f"{RED}This text is Red!{RESET}")
print(f"{GREEN}This text is Green!{RESET}")
print(f"{YELLOW}This text is Yellow!{RESET}")


print("\033[31m This text is Red! \033[0m")
print("\033[1;32m This text is Bold Green! \033[0m")



def read_engagement():
    """Read every valid engagement record and return a list."""

    # Empty list for engagement dictionaries.
    engagement_records = []

    try:
        # Open the engagement file in read mode.
        with open(ENGAGEMENT_FILE, "r", encoding="utf-8") as file:

            # Read each line from the file.
            for line in file:
                line = line.strip()

                # Continue only when the line contains data.
                if line:
                    parts = line.split("|")

                    # Each engagement record has five fields.
                    if len(parts) == 5:
                        engagement_records.append({
                            "post_id": parts[0],

                            # Convert numeric text into integers so that the
                            # values can later be added and compared.
                            "likes": int(parts[1]),
                            "comments": int(parts[2]),
                            "shares": int(parts[3]),
                            "views": int(parts[4])
                        })

    except FileNotFoundError:
        # Create the file when it is missing.
        open(ENGAGEMENT_FILE, "w", encoding="utf-8").close()

    return engagement_records
