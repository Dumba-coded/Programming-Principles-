print("1. Add New Post")
print("2. Update Post Status")
print("3. Record Engagement Metrics")
print("4. Display Content Calendar")
print("5. Generate Performance Report")
print("6. Export Report to File")
print("7. Exit")
chosen = int(input("Enter your choice: "))

if chosen == '1':
  post_id = str(input("Enter Post ID: "))
  platform = str(input("Enter Platform: " ))
  caption = str(input("Enter Caption: "))
  scheduled_date = date(input("Enter Scheduled Date: "))

  with open("posts.txt", "a", encoding="utf-8") as postfile:
    postfile.write(f'{post_id}|{platform}|{caption}|{scheduled_date}\n')
  print("Post added successfully.")
  #status = draft ??

elif chosen == '2':
  def read_posts():
    posts = []
    with open("posts.txt","r") as file:
        for line in file:
            line = line.strip()
            if line:
                fields = line.split("|")
                posts.append(fields)
    return posts
  
  def write_posts(posts):
     with open("posts.txt","w") as file:
        for post in posts:
          file.write("|".join(post) + "\n")

  def show_available_posts(posts):
     print("\nAvailable Posts")
     for post in posts:
        post_id = post[0]
        status = post[4]
        print(f"{post_id} - {status}")

  def update_status():
    posts = read_posts()
    if not posts:
      print("No posts found.")
      return

  def show_available_posts(posts):
    post_id = input("\nEnter Post ID: ").strip().uppar()
    found_post = None
    for post in posts:
       if post[0].uppar() == post_id:
          found_post = post
          break
    if found_post is None:
       print("Post ID not found.")

    current_status = found_post[4]
    print(f"\nCurrent Status: {current_status}")

    print("1. Schedule")
    print("2. Posted.")
    choice = input("Choose new status: ").strip()

    if choice == "1":
       new_status = "Scheduled"
    elif choice == "2":
      new_status = "Posted"
    else:
      print("Invalid choice. Status not changed.")
      return

    found_post[4] = new_status
    write_posts(posts)
    print("\nStatus updated successfuly.")
    print("File becomes:")
    print("|".join(found_post))

  if __name__ == "__main__":
    update_status()

elif chosen == 3:
  def read_post():
     posts = []
     with open("posts.txt","r") as file:
        for line in file:
          line = line.strip()
          if line:
            posts.append(line.split("|"))
    return posts #error

  def get_number(prompt):
     while True:
        value = input(prompt).strip()
        if value.isdigit():
           return value 
        print("Please enter a whole number.")

  def record_engagement():
    posts = read_posts()

    if not posts:
      print("No posts found.")
      return
    print("Only for Posted posts.")
    post_id = input("ENter Post ID: ").strip().upper()

    found_post = None
    for post in posts:
      if post[0].uppar() == post_id:
        found_post = post
        break
    if found_post is None:
      print("Post ID not found.")
      return

    if found_post[4] != "Posted":
      print(f"Cannot record engagement. Post status is '{found_post[4]}', not 'Posted'.")
      return 

    print()
    likes = get_number("Likes: ")
    comments = get_number("Comments: ")
    shares = get_number("Shares: ")
    views = get_number("Views: ")
    engagement_line = "|".join([found_post[0], likes, comment, shares, views])

    with open("engagement.txt","a") as file:
      file.write(engagement_line + "\n")
    print("\nEngagement recorded successfully.")
    print("engagement.txt")
    print(engagement_line)

  if __name__ == "__main__":
    record_engagement() 
elif chosen == "4":
  def read_posts():
    posts = []
    with open("posts.txt", "r") as file:
      for line in file:
        line = line.strip()
        if line:
          posts.append(line.split("|"))
    return posts

  def display_calender():
    posts = read_posts()

    if not posts:
      print("No posts found.")
