from datetime import datetime

# File names
POST_FILE = "posts.txt"
ENGAGEMENT_FILE = "engagement.txt"
PLATFORM_FILE = "platforms.txt"


# ---------------- add_post ----------------
def add_post():
    
    print("\n--- Add New Post ---")
    
    # 1. Get Post ID (must not be empty)
    post_id = input("Enter Post ID: ").upper()
    if post_id.strip() == "":
        print("Invalid input. Post ID cannot be empty.")
        return
    
    # 2. Get Platform (must be one of the 3 allowed platforms)
    platform = input("Enter Platform (Instagram / TikTok / X): ")
    if platform not in ["Instagram", "TikTok", "X"]:
        print("Invalid platform. Must be Instagram, TikTok, or X.")
        return
    
    # 3. Get Caption (must not be empty)
    caption = input("Enter Caption: ")
    if caption.strip() == "":
        print("Invalid input. Caption cannot be empty.")
        return
    
    # 4. Get Scheduled Date (must be a real date in DD-MM-YYYY format)
    date = input("Enter Scheduled Date (DD-MM-YYYY): ")
    try:
        datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        print("Invalid date. Please use format DD-MM-YYYY.")
        return

    # 5. New post is Draft by default
    status = "Draft"
    
    # 6. Save into posts.txt
    with open(POST_FILE, "a") as file:
        file.write(post_id + "|" +
                   platform + "|" +
                   caption + "|" +
                   date + "|" +
                   status + "\n")
    
    print("Post added successfully!")


# ---------------- update_status ----------------
def update_post():
    
    # 1. Read all existing posts from the file
    try:
        with open(POST_FILE, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No posts found. Please add a post first.")
        return
 
    if len(lines) == 0:
        print("No posts found. Please add a post first.")
        return
 
    # 2. Show all available posts with their current status
    print("\nAvailable Posts")
    for line in lines:
        fields = line.strip().split("|")
        print(fields[0] + " - " + fields[4])
 
    # 3. Ask which Post ID to update
    target_id = input("\nEnter Post ID: ").upper()
 
    # 4. Find the matching post
    found = False
    for line in lines:
        fields = line.strip().split("|")
        if fields[0] == target_id:
            found = True
            current_status = fields[4]
            break
 
    if not found:
        print("Post ID not found.")
        return
 
    print("Current Status: " + current_status)
 
    # 5. Only allow the correct next status
    if current_status == "Draft":
        print("1. Scheduled")
        print("2. Posted")
        new_choice = input("Choose new status (1 or 2): ")
        if new_choice == "1":
            new_status = "Scheduled"
        else:
            print("Invalid choice. Draft can only move to Scheduled.")
            return
 
    elif current_status == "Scheduled":
        print("1. Scheduled")
        print("2. Posted")
        new_choice = input("Choose new status (1 or 2): ")
        if new_choice == "2":
            new_status = "Posted"
        else:
            print("Invalid choice. Scheduled can only move to Posted.")
            return
 
    else:
        print("This post is already Posted. No further update possible.")
        return
 
    # 6. Rebuild the file with the updated status for the matching post
    with open(POST_FILE, "w") as file:
        for line in lines:
            fields = line.strip().split("|")
            if fields[0] == target_id:
                fields[4] = new_status
            file.write("|".join(fields) + "\n")
 
    print("Status updated successfully.")
    
    
# ---------------- Main Menu ----------------
def menu():
    print("\n========== SOCIAL MEDIA CONTENT PLANNER ==========")
    print("1. Add New Post")
    print("2. Update Post Status")
    print("3. Record Engagement Metrics")
    print("4. Display Content Calendar")
    print("5. Generate Performance Report")
    print("6. Export Report to File")
    print("7. Exit")


# ---------------- Main Program ----------------
while True:
    menu()
    choice = input("Enter your choice (1-7): ")
    if choice == "1":
        add_post()
    elif choice == "2":
        update_post()
    elif choice == "3":
        engagement_metrics()
    elif choice == "4":
        content_calendar()
    elif choice == "5":
        performance_report()
    elif choice == "6":
        export_report()
    elif choice == "7":
        exit_plan()
        break
    else:
        print("Invalid choice. Please try again.")
