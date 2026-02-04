#!/usr/bin/python3
"""
Task 0: Simple templating program
Generates invitation files from a template and a list of attendee dictionaries.
"""

from __future__ import annotations

import os
from typing import Any


def generate_invitations(template: Any, attendees: Any) -> None:
    """
    Generate output_X.txt invitation files using `template` and `attendees`.

    Rules:
    - template must be a non-empty string
    - attendees must be a non-empty list of dictionaries
    - Missing or None values for placeholders become "N/A"
    - Output files are named output_1.txt, output_2.txt, ... (1-based index)
    """
    # ---- Validate input types ----
    if not isinstance(template, str):
        print(f"Invalid input type: template must be a string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or any(not isinstance(a, dict) for a in attendees):
        got_type = type(attendees).__name__
        print("Invalid input type: attendees must be a list of dictionaries, "
              f"got {got_type} (and/or contains non-dict items).")
        return

    # ---- Handle empty inputs ----
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Placeholders we expect to replace
    fields = ["name", "event_title", "event_date", "event_location"]

    # ---- Generate files ----
    for idx, attendee in enumerate(attendees, start=1):
        # Build replacement values, using "N/A" for missing keys or None
        values = {}
        for key in fields:
            val = attendee.get(key, "N/A")
            if val is None:
                val = "N/A"
            values[key] = str(val)

        # Replace placeholders (explicitly using replace as hinted)
        content = template
        for key in fields:
            content = content.replace("{" + key + "}", values[key])

        filename = f"output_{idx}.txt"

        # If file exists, avoid overwriting by finding the next available name
        if os.path.exists(filename):
            n = idx
            while os.path.exists(f"output_{n}.txt"):
                n += 1
            filename = f"output_{n}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
        except OSError as e:
            print(f"Error writing file {filename}: {e}")
            # Continue to next attendee rather than crashing
            continue
