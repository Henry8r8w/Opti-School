from models import add_recipient

recipients = [
    ("youremail@gamil.com", "FirstName LastName"),
]

for recipient_email, representative in recipients:
    add_recipient(recipient_email, entity, representative)

print("all recipients added successfully")
