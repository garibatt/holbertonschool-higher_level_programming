import os

def generate_invitations(template, attendees):
    # documentation
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees must be a list of dictionaries, got {type(attendees).__name__}")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template[:]

        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder)
            if not value:
                value = "N/A"
            invitation = invitation.replace(f"{{{placeholder}}}", str(value))

        output_filename = f"output_{index}.txt"

        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(invitation)
            print(f"Generated {output_filename}")
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")

