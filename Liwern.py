
from datetime import date

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

#----------------------------------------#
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

    with open("performance_report.txt", "w") as file:
        file.write(report)

    print("Report exported successfully!")

    
  
#----------------------------------------#
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
            export_report(instagram_count, tiktok_count, x_count,
                best_post_id, best_platform, best_total,
                most_interactive_platform, highest_engagement) #appears here 
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")




main()# runs forevrrrrr, Keeps running the menu after all commands are done until the user chooses Exit
