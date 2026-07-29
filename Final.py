from datetime import datetime

POST_FILE = "posts.txt"
ENGAGEMENT_FILE = "engagement.txt"
# REPORT_FILE = "report.txt"



# -----Exit the program gracefully with a goodbye message -----
def exit_program():
    print("\nThanks for using the Social Media Planner. Goodbye!")
    exit() # A built-in function that terminates the program immediately.

# Save original input
original_input = input

# Safe input function
def safe_input(prompt): # prompt = the text you pass when asking the user for input
    user_input = original_input(prompt)  # whatever the user types will be stored in 'user_input'
    if user_input.lower() in ["cancel", "exit", "end"]: #converts input to lowercase
        exit_program()
    return user_input

# Override input globally
input = safe_input # Replaces Python's built-in 'input' function with safe_input




# ----- Display all seven program options -----
def display_menu():
    
    print("\n=====================================")
    print("SOCIAL MEDIA CONTENT PLANNER")
    print("=====================================")
    print("1. Add New Post")
    print("2. Update Post Status")
    print("3. Record Engagement Metrics")
    print("4. Display Content Calendar")
    print("5. Generate Performance Report")
    print("6. Export Report to File")
    print("7. Exit")# change to "Press X/type [keyword] (ex.exit) to exit the programm at any given moment"




# ----- Add a new post to the posts.txt file -----
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

    # Check if this Post ID already exists in posts.txt
    try:
        with open(POST_FILE, "r") as file:
            existing_lines = file.readlines()
        for line in existing_lines:
            fields = line.strip().split("|")
            if fields[0] == post_id:
                print("This Post ID already exists.")
                return
    except FileNotFoundError:
        pass # No file yet means no existing posts, so it's fine to continue

    # 2. Get Platform (must be one of the 3 allowed platforms)
    platform = input("Enter Platform (Instagram / TikTok / X): ").strip().capitalize()
    
    Platform_input = platform.lower()
    
    platform_names = {
        "instagram": "Instagram",
        "tiktok": "TikTok",
        "x": "X"} 
    
    if Platform_input not in platform_names:
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




# ----- Update the status of an existing post -----
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




# ----- Allow user to record engagement metrics for a specific post -----
def record_engagement_metrics():
    
    print(f"\n--- RECORD ENGAGEMENT METRICS ---")




# ----- Show the content calendar with all posts and their statuses -----
def display_content_calendar():

    try:
        with open(POST_FILE, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No posts found.")
        return

    if len(lines) == 0:
        print("No posts found.")
        return

    print("\n=========================================================")
    print(f"{'POST_ID':<10}{'DATE':<13}{'PLATFORM':<15}{'STATUS'}")
    print("=========================================================")

    for line in lines:
        fields = line.strip().split("|")

        post_id = fields[0]
        platform = fields[1]
        date = fields[3].replace("-", "/")   # Changes DD-MM-YYYY to DD/MM/YYYY
        status = fields[4]

        print(f"{post_id:<10}{date:<13}{platform:<15}{status}")

    print("=========================================================")




# ----- Display a summary of engagement metrics for all posts -----
def generate_performance_report():

    # 1. Read posts.txt (we need the platform of every post)
    try:
        with open(POST_FILE, "r") as post_file:
            post_lines = post_file.readlines()
    except FileNotFoundError:
        print("No posts found. Please add a post first.")
        return

    # 2. Count how many posts belong to each platform
    instagram_count = 0
    tiktok_count = 0
    x_count = 0

    for line in post_lines:
        fields = line.strip().split("|")
        post_platform = fields[1]

        if post_platform == "Instagram":
            instagram_count = instagram_count + 1
        elif post_platform == "TikTok":
            tiktok_count = tiktok_count + 1
        elif post_platform == "X":
            x_count = x_count + 1

    # 3. Read engagement.txt (we need likes, comments, shares, views)
    try:
        with open(ENGAGEMENT_FILE, "r") as engagement_file:
            engagement_lines = engagement_file.readlines()
    except FileNotFoundError:
        print("No engagement data found. Please record engagement first.")
        return

    # 4. Go through every engagement record to find the best post
    best_post_id = ""
    best_platform = ""
    best_total = -1

    instagram_engagement = 0
    tiktok_engagement = 0
    x_engagement = 0

    for e_line in engagement_lines:
        e_fields = e_line.strip().split("|")
        post_id = e_fields[0]
        likes = int(e_fields[1])
        comments = int(e_fields[2])
        shares = int(e_fields[3])
        views = int(e_fields[4])

        total_engagement = likes + comments + shares + views

        # Find out which platform this post belongs to
        # By searching through the posts we read earlier
        platform_of_this_post = ""
        for p_line in post_lines:
            p_fields = p_line.strip().split("|")
            if p_fields[0] == post_id:
                platform_of_this_post = p_fields[1]

        # Add this post's engagement to its platform's total
        if platform_of_this_post == "Instagram":
            instagram_engagement = instagram_engagement + total_engagement
        elif platform_of_this_post == "TikTok":
            tiktok_engagement = tiktok_engagement + total_engagement
        elif platform_of_this_post == "X":
            x_engagement = x_engagement + total_engagement

        # Check if this post is the best one so far
        if total_engagement > best_total:
            best_total = total_engagement
            best_post_id = post_id
            best_platform = platform_of_this_post

    # 5. Work out which platform has the most total interaction
    most_interactive_platform = "Instagram"
    highest_engagement = instagram_engagement

    if tiktok_engagement > highest_engagement:
        most_interactive_platform = "TikTok"
        highest_engagement = tiktok_engagement

    if x_engagement > highest_engagement:
        most_interactive_platform = "X"
        highest_engagement = x_engagement

    # 6. Print the report
    print("\n=====================================")
    print("PERFORMANCE REPORT")
    print("=====================================")
    print("Total Posts Per Platform")
    print("Instagram : " + str(instagram_count))
    print("TikTok : " + str(tiktok_count))
    print("X : " + str(x_count))

    print("\nBest Performing Post")
    print("Post ID : " + best_post_id)
    print("Platform: " + best_platform)
    print("Total Engagement: " + str(best_total))

    print("\nMost Interactive Platform")
    print(most_interactive_platform)

    return (instagram_count, tiktok_count, x_count,
            best_post_id, best_platform, best_total,
            most_interactive_platform, highest_engagement)




# ----- Export the performance report to a text file -----
def export_report(instagram_count, tiktok_count, x_count,
                best_post_id, best_platform, best_total,
                most_interactive_platform, highest_engagement):
    
    report = "=====================================\n"
    report += "PERFORMANCE REPORT\n"
    report += "=====================================\n"
    report += "Total Posts Per Platform\n"
    report += f"Instagram : {instagram_count}\n"
    report += f"TikTok    : {tiktok_count}\n"
    report += f"X         : {x_count}\n\n"

    report += "Best Performing Post\n"
    report += f"Post ID   : {best_post_id}\n"
    report += f"Platform  : {best_platform}\n"
    report += f"Total Engagement: {best_total}\n\n"

    report += "Most Interactive Platform\n"
    report += f"{most_interactive_platform} (Total Engagement: {highest_engagement})\n"

    with open("report.txt", "w") as file:
        file.write(report)

    print("Report exported successfully!")




# ----- Main program -----
def main():

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        # Call the function connected to the selected option
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
            results = generate_performance_report()
            if results:
                export_report(*results)  # Unpack the results and pass them to export_report
        elif choice == "7":
            exit_program()
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

main() # Runs forevrrrrr, Keeps running the menu after all commands are done until the user chooses Exit

