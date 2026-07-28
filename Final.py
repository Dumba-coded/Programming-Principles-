RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'

POSTS_FILE = "posts.txt"
ENGAGEMENT_FILE = "engagement.txt"
REPORT_FILE = "report.txt"


def read_posts():
    """Read every valid post record from posts.txt and return a list."""

    posts = []

    try:

        # "with" closes the file automatically after the block finishes.
        with open(POSTS_FILE, "r", encoding="utf-8") as file:

            for line in file:

                # Remove spaces and the newline character from both ends.
                line = line.strip()
                # Ignore empty lines.
                if line:
                    parts = line.split("|")

                    # A complete post must contain exactly five fields.
                    if len(parts) == 5:

                        # Dictionary is not in our sykkbaus but essentially just a list with attributes
                        posts.append({
                            "post_id": parts[0],
                            "platform": parts[1],
                            "caption": parts[2],
                            "scheduled_date": parts[3],
                            "status": parts[4]
                        })

    #Handle the error that occurs when the file does not exist.
    except FileNotFoundError:

        # Create an empty file, then close it immediately.
        open(POSTS_FILE, "w", encoding="utf-8").close()

    # Send the completed list back to the function that called read_posts().
    return posts

def save_posts(posts):
    """Save all post records to posts.txt."""

    # Open in write mode. Existing contents are replaced.
    with open(POSTS_FILE, "w", encoding="utf-8") as file:
        for post in posts:

            # Convert one post into a | separated text line.
            file.write(
                f"{post['post_id']}|{post['platform']}|"
                f"{post['caption']}|{post['scheduled_date']}|"
                f"{post['status']}\n"
            )
            
def read_engagement():
    """Read every valid engagement record and return a list."""

    engagement_records = []

    try:
        # Open the engagement file in read mode since it doesn't need TO edited
        with open(ENGAGEMENT_FILE, "r", encoding="utf-8") as file:

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

#takes attribute from the top funciton
def save_engagement(engagement_records):
    """Save all engagement records to engagement.txt."""

    with open(ENGAGEMENT_FILE, "w", encoding="utf-8") as file:
        for record in engagement_records:
            file.write(
                f"{record['post_id']}|{record['likes']}|"
                f"{record['comments']}|{record['shares']}|"
                f"{record['views']}\n"
            )
            

def display_menu():
    """Display all seven program options."""

    print("\n=====================================")
    print("SOCIAL MEDIA CONTENT PLANNER")
    print("=====================================")
    print("1. Add New Post")
    print("2. Update Post Status")
    print("3. Record Engagement Metrics")
    print("4. Display Content Calendar")
    print("5. Generate Performance Report")
    print("6. Export Report to File")
    print("7. Exit")# change to "Presx/type [keyword] (ex.exit) to exit the programm at any given moment"


def add_new_post():
    """Add a new post with Draft status."""

    # Load existing posts before adding another one.
    posts = read_posts()

    print("\n--- ADD NEW POST ---")

    # Get the ID, remove outside spaces, and convert letters to uppercase.
    post_id = input("Enter Post ID: ").strip().upper()

    # Stop the function when the ID is empty.
    if post_id == "":
        print("Post ID cannot be empty.")
        return

    # Search existing posts to prevent duplicate IDs.
    for post in posts:
        if post["post_id"] == post_id:
            print("Post ID already exists.")
            return

    # Collect the remaining post information.
    platform = input("Enter Platform (Tiktok/Instagram/X): ").strip()
    caption = input("Enter Caption: ").strip()
    scheduled_date = input("Enter Scheduled Date (DD/MM/YYYY): ").strip()

    # Platform and caption are required fields.
    if platform == "" or caption == "":
        print("Platform and caption cannot be empty.")
        return

    # Call a date-validation function If we need it/ DO WE NEED IT ???


    # Create the new post as a dictionary.
    new_post = {
        "post_id": post_id,
        "platform": platform,
        "caption": caption,
        "scheduled_date": scheduled_date,
        "status": "Draft"
    }

    # Add the dictionary to the list and save the updated list.
    posts.append(new_post)
    save_posts(posts)

    print("Post added successfully.")
    print("Status: Draft")

    
def update_post_status():
    print
    
def record_engagement_metrics():
    
    print(f"{YELLOW}\n--- RECORD ENGAGEMENT METRICS ---{RESET}")

    

    
    
    
    
def display_content_calendar():
    print

def generate_performance_report():
    print
    
def export_report_to_file():
    print
    
    """If We manage to allow user to exit at any given moment this will be a function as well"""
def Exit():
    print(f"{YELLOW}Program ended successfully.{RESET}")

def main():

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        # Call the function connected to the selected option.
        if choice == "1":
            add_new_post()
        elif choice == "2":
            update_post_status()
        elif choice == "3":
            record_engagement_metrics()
        elif choice == "4":
            display_content_calendar()
        elif choice == "5":
            generate_performance_report()
        elif choice == "6":
            export_report_to_file()
        elif choice == "7":
            Exit()
            break
        else:
            print(f"{RED}Invalid choice. Please enter a number from 1 to 7.{RESET}")

main()# runs forevrrrrr, Keeps running the menu after all commands are done until the user chooses Exit

