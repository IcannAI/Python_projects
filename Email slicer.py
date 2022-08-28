# Using the user input and strip function 
# Using '@' symbol as the separator to split the email into two parts
email = input("Type your email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@") + 1:]
format_ = (f"Your name is'{username}' and your domain is '{domain_name}'")
print(format_)