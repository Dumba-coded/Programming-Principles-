from datetime import datetime


def exit_program(): #lw
    print("\nThanks for using the Social Media Planner. Goodbye!")
    exit() # A built-in function that terminates the program immediately.


# Save original input
original_input = input


# Safe input function
def safe_input(prompt): #prompt = the text you pass when asking the user for input
    user_input = original_input(prompt)  #whatever the user types will be stored in 'user_input'
    if user_input.lower() in ["x", "exit", "end"]: #converts input to lowercase
        exit_program()
    return user_input


# Override input globally
input = safe_input #replaces Python's built-in 'input' function with safe_input

POST_FILE = "posts.txt"
ENGAGEMENT_FILE = "engagement.txt"
REPORT_FILE = "report.txt"


# Display all seven program options.
def display_menu():
    
    print("\n========== SOCIAL MEDIA CONTENT PLANNER ==========")
    print("1. Add New Post")
    print("2. Update Post Status")
    print("3. Record Engagement Metrics")
    print("4. Display Content Calendar")
    print("5. Generate Performance Report")
    print("6. Export Report to File")
    print("7. Exit")# change to "Press X/type [keyword] (ex.exit) to exit the programm at any given moment"


# Add a new post to the posts.txt file.
def add_post():
    
    print("\n--- Add New Post ---")
    
    # 1. Get Post ID (must not be empty)
    post_id = input("Enter Post ID: ").upper()
    
    if post_id.strip() == "":
        print("Invalid input. Post ID cannot be empty.")
        return
    if not post_id.startswith("P"):
        print("Invalid Post ID. Post ID must start with 'P' (e.g. P011).")
        return


    # 2. Get Platform (must be one of the 3 allowed platforms)
    platform = input("Enter Platform (Instagram / TikTok / X): ")
    
    platform_names = {
        "instagram": "Instagram",
        "tiktok": "TikTok",
        "x": "X"} 
    
    if platform not in platform_names:
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


# Update the status of an existing post.
def update_post():
    
    # 1. Read all existing posts from the file
    try:
        with open(POST_FILE, "r") as file:
            lines = file.readlines()
    except FileNotFoundError: # Catch the error if the file does not exist
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


# Allow user to record engagement metrics for a specific post.
def record_engagement_metrics():
    
    print(f"{YELLOW}\n--- RECORD ENGAGEMENT METRICS ---{RESET}")
    

# Show the content calendar with all posts and their statuses.
def display_content_calendar():
    print


# Display a summary of engagement metrics for all posts.
def generate_performance_report():
    print


# Export the performance report to a text file.
def export_report():
    posts_per_platform, best_post, most_interactive_platform, total_posts, avg_engagement = generate_report()
    report = "=== PERFORMANCE REPORT ===\n"
    report += f"Generated on: {date.today()}\n\n"

    report += "Posts per Platform:\n"

    for platform, data in posts_per_platform.items():
        report += f"{platform:<10}: {data['posts']} post (Followers: {data['followers']})\n"

    report += "\n"
    report += f"Best Post: {best_post['id']} ({best_post['platform']}, {best_post['likes']} likes, {best_post['shares']} shares)\n"
    report += f"Most Interactive Platform: {most_interactive_platform['name']} (Total Engagement: {most_interactive_platform['engagement']})\n"

    report += "\nOverall Stats:\n"
    report += f"Total Posts: {total_posts}\n"
    report += f"Average Engagement per Post: {avg_engagement}\n"

    with open("report.txt", "w") as file:
        file.write(report)

    print("Report exported successfully!")

    


def main():

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        # Call the function connected to the selected option.
        if choice == "1":
            add_post()
        elif choice == "2":
            update_post()
        elif choice == "3":
            record_engagement_metrics()
        elif choice == "4":
            display_content_calendar()
        elif choice == "5":
            generate_performance_report()
        elif choice == "6":
            export_report()
        elif choice == "7":
            Exit()
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")




main() # Runs forevrrrrr, Keeps running the menu after all commands are done until the user chooses Exit

