#!/usr/bin/env python3

import argparse
import os

class ProjectTemplate():
    
    def get_base_structure():
        return [
            "1. CODES",
            "2. NOTES",
            "3. MEETING",
            "4. PPT",
            "5. TEST",
            "6. UI",
            "7. OTHERS"
        ]

parser = argparse.ArgumentParser()
proj_template = ProjectTemplate()

parser.add_argument(
    "project_name",
    type=str,
    help="Create a new structure project")

args = parser.parse_args()

for dir_name in ProjectTemplate.get_base_structure():
    destination = os.path.join(args.project_name, dir_name)
    if not os.path.exists(destination):
        os.makedirs(destination, exist_ok=True)