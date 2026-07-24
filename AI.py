from datetime import datetime

POSTS_FILE = "posts.txt"
ENGAGEMENT_FILE = "engagement.txt"
REPORT_FILE = "report.txt"


def read_posts():
    """Read all posts from posts.txt."""
    posts = []

    try:
        with open(POSTS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line:
                    parts = line.split("|")

                    if len(parts) == 5:
                        posts.append({
                            "post_id": parts[0],
                            "platform": parts[1],
                            "caption": parts[2],
                            "scheduled_date": parts[3],
                            "status": parts[4]
                        })

    except FileNotFoundError:
        open(POSTS_FILE, "w", encoding="utf-8").close()

    return posts


def save_posts(posts):
    """Save all posts to posts.txt."""
    with open(POSTS_FILE, "w", encoding="utf-8") as file:
        for post in posts:
            file.write(
                f"{post['post_id']}|{post['platform']}|"
                f"{post['caption']}|{post['scheduled_date']}|"
                f"{post['status']}\n"
            )


def read_engagement():
    """Read engagement records from engagement.txt."""
    engagement_records = []

    try:
        with open(ENGAGEMENT_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line:
                    parts = line.split("|")

                    if len(parts) == 5:
                        engagement_records.append({
                            "post_id": parts[0],
                            "likes": int(parts[1]),
                            "comments": int(parts[2]),
                            "shares": int(parts[3]),
                            "views": int(parts[4])
                        })

    except FileNotFoundError:
        open(ENGAGEMENT_FILE, "w", encoding="utf-8").close()

    return engagement_records


def save_engagement(engagement_records):
    """Save engagement records to engagement.txt."""
    with open(ENGAGEMENT_FILE, "w", encoding="utf-8") as file:
        for record in engagement_records:
            file.write(
                f"{record['post_id']}|{record['likes']}|"
                f"{record['comments']}|{record['shares']}|"
                f"{record['views']}\n"
            )


def valid_date(date_text):
    """Check whether a date follows DD/MM/YYYY format."""
    try:
        datetime.strptime(date_text, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def get_non_negative_integer(message):
    """Request a valid non-negative whole number."""
    while True:
        try:
            value = int(input(message))

            if value < 0:
                print("Value cannot be negative.")
            else:
                return value

        except ValueError:
            print("Please enter a valid whole number.")


def add_new_post():
    """Option 1: Add a new post with Draft status."""
    posts = read_posts()

    print("\n--- ADD NEW POST ---")

    post_id = input("Enter Post ID: ").strip().upper()

    if post_id == "":
        print("Post ID cannot be empty.")
        return

    for post in posts:
        if post["post_id"] == post_id:
            print("Post ID already exists.")
            return

    platform = input("Enter Platform: ").strip()
    caption = input("Enter Caption: ").strip()
    scheduled_date = input(
        "Enter Scheduled Date (DD/MM/YYYY): "
    ).strip()

    if platform == "" or caption == "":
        print("Platform and caption cannot be empty.")
        return

    if not valid_date(scheduled_date):
        print("Invalid date. Please use DD/MM/YYYY.")
        return

    new_post = {
        "post_id": post_id,
        "platform": platform,
        "caption": caption,
        "scheduled_date": scheduled_date,
        "status": "Draft"
    }

    posts.append(new_post)
    save_posts(posts)

    print("Post added successfully.")
    print("Status: Draft")


def update_post_status():
    """Option 2: Update a post from Draft to Scheduled or Posted."""
    posts = read_posts()

    if not posts:
        print("\nNo posts are available.")
        return

    print("\n--- UPDATE POST STATUS ---")
    print("Available Posts")

    for post in posts:
        print(f"{post['post_id']} - {post['status']}")

    post_id = input("Enter Post ID: ").strip().upper()

    selected_post = None

    for post in posts:
        if post["post_id"] == post_id:
            selected_post = post
            break

    if selected_post is None:
        print("Post not found.")
        return

    print(f"Current Status: {selected_post['status']}")
    print("1. Scheduled")
    print("2. Posted")

    choice = input("Choose new status: ").strip()

    if choice == "1":
        selected_post["status"] = "Scheduled"
    elif choice == "2":
        selected_post["status"] = "Posted"
    else:
        print("Invalid choice.")
        return

    save_posts(posts)
    print("Status updated successfully.")


def record_engagement_metrics():
    """Option 3: Record engagement only for a Posted post."""
    posts = read_posts()
    engagement_records = read_engagement()

    print("\n--- RECORD ENGAGEMENT METRICS ---")

    post_id = input("Enter Post ID: ").strip().upper()

    selected_post = None

    for post in posts:
        if post["post_id"] == post_id:
            selected_post = post
            break

    if selected_post is None:
        print("Post not found.")
        return

    if selected_post["status"] != "Posted":
        print("Engagement can only be recorded for Posted posts.")
        return

    likes = get_non_negative_integer("Likes: ")
    comments = get_non_negative_integer("Comments: ")
    shares = get_non_negative_integer("Shares: ")
    views = get_non_negative_integer("Views: ")

    existing_record = None

    for record in engagement_records:
        if record["post_id"] == post_id:
            existing_record = record
            break

    if existing_record:
        existing_record["likes"] = likes
        existing_record["comments"] = comments
        existing_record["shares"] = shares
        existing_record["views"] = views
    else:
        engagement_records.append({
            "post_id": post_id,
            "likes": likes,
            "comments": comments,
            "shares": shares,
            "views": views
        })

    save_engagement(engagement_records)
    print("Engagement recorded successfully.")


def display_content_calendar():
    """Option 4: Display all posts sorted by scheduled date."""
    posts = read_posts()

    if not posts:
        print("\nNo posts are available.")
        return

    posts.sort(
        key=lambda post: datetime.strptime(
            post["scheduled_date"], "%d/%m/%Y"
        )
    )

    print("\n" + "=" * 70)
    print(
        f"{'POST ID':<12}"
        f"{'DATE':<15}"
        f"{'PLATFORM':<18}"
        f"{'STATUS':<15}"
        f"{'CAPTION'}"
    )
    print("=" * 70)

    for post in posts:
        caption_preview = post["caption"][:25]

        print(
            f"{post['post_id']:<12}"
            f"{post['scheduled_date']:<15}"
            f"{post['platform']:<18}"
            f"{post['status']:<15}"
            f"{caption_preview}"
        )

    print("=" * 70)


def create_performance_report():
    """Create and return the required performance report."""
    posts = read_posts()
    engagement_records = read_engagement()

    platform_post_counts = {}
    platform_interactions = {}

    for post in posts:
        platform = post["platform"]

        if platform not in platform_post_counts:
            platform_post_counts[platform] = 0

        platform_post_counts[platform] += 1

    best_post_id = "No engagement data"
    best_post_platform = "-"
    highest_engagement = -1

    for record in engagement_records:
        total_engagement = (
            record["likes"]
            + record["comments"]
            + record["shares"]
        )

        post_platform = "Unknown"

        for post in posts:
            if post["post_id"] == record["post_id"]:
                post_platform = post["platform"]
                break

        if post_platform not in platform_interactions:
            platform_interactions[post_platform] = 0

        platform_interactions[post_platform] += total_engagement

        if total_engagement > highest_engagement:
            highest_engagement = total_engagement
            best_post_id = record["post_id"]
            best_post_platform = post_platform

    if platform_interactions:
        most_interactive_platform = max(
            platform_interactions,
            key=platform_interactions.get
        )
    else:
        most_interactive_platform = "No engagement data"

    report_lines = [
        "=====================================",
        "PERFORMANCE REPORT",
        "=====================================",
        "Total Posts Per Platform"
    ]

    if platform_post_counts:
        for platform, total in platform_post_counts.items():
            report_lines.append(f"{platform} : {total}")
    else:
        report_lines.append("No posts available")

    report_lines.extend([
        "",
        "Best Performing Post",
        f"Post ID : {best_post_id}",
        f"Platform: {best_post_platform}"
    ])

    if highest_engagement >= 0:
        report_lines.append(
            f"Total Engagement: {highest_engagement}"
        )
    else:
        report_lines.append("Total Engagement: 0")

    report_lines.extend([
        "",
        "Most Interactive Platform",
        most_interactive_platform
    ])

    return "\n".join(report_lines)


def generate_performance_report():
    """Option 5: Display the performance report."""
    print("\n" + create_performance_report())


def export_report_to_file():
    """Option 6: Export the performance report to report.txt."""
    report = create_performance_report()

    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        file.write(report)

    print("\nReport exported successfully to report.txt.")


def display_menu():
    """Display the seven required menu options."""
    print("\n=====================================")
    print("SOCIAL MEDIA CONTENT PLANNER")
    print("=====================================")
    print("1. Add New Post")
    print("2. Update Post Status")
    print("3. Record Engagement Metrics")
    print("4. Display Content Calendar")
    print("5. Generate Performance Report")
    print("6. Export Report to File")
    print("7. Exit")


def main():
    """Run the menu until the user selects Exit."""
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

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
            print("Program ended successfully.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
