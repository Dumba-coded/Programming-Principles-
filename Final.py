
from datetime import date #lw

def exit_program(): #lw
    print("\nThanks for using the Social Media Planner. Goodbye!")
    exit() #a built-in function that terminates the program immediately.

# save original input
original_input = input

# safe input function
def safe_input(prompt): #prompt = the text you pass when asking the user for input
    user_input = original_input(prompt)  #whatever the user types will be stored in 'user_input'
    if user_input.lower() in ["x", "exit", "end"]: #converts input to lowercase
        exit_program()
    return user_input

# override input globally
input = safe_input #replaces Python's built-in 'input' function with safe_input


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
    print
    
def update_post_status():
    print
    
def record_engagement_metrics():
    print
    
def display_content_calendar():
    print

def generate_performance_report():
    print
    
def export_report(): #lw
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
            export_report()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")




main()# runs forevrrrrr, Keeps running the menu after all commands are done until the user chooses Exit

