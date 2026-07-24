


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
    
def export_report_to_file():
    print
    
    """If We manage to allow user to exit at any given moment this will be a function as well"""
def Exit():
    print("Program ended successfully.")

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
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

main()# runs forevrrrrr, Keeps running the menu after all commands are done until the user chooses Exit

