#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":

    settings = 'app.settings.dev'
    for match in sys.argv:
        if match.startswith('--settings'):
            settings = match.split('=')[1]

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
