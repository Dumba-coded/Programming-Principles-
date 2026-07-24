RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'

print(f"{RED}This text is Red!{RESET}")
print(f"{GREEN}This text is Green!{RESET}")
print(f"{YELLOW}This text is Yellow!{RESET}")


print("\033[31m This text is Red! \033[0m")
print("\033[1;32m This text is Bold Green! \033[0m")

