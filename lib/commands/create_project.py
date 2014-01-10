#  Coop a tool to deploy and socialize Python projects
#   Copyright (C) 2013  Juan Manuel Schillaci
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
# Coop version 0.1, Copyright (C) 2013  Juan Manuel Schillaci
#   Coop comes with ABSOLUTELY NO WARRANTY.
#   This is free software, and you are welcome to redistribute it
#   under certain conditions;
import os
import sys

from yapsy.IPlugin import IPlugin


def sanitize_name(name):
    return name


class Command(IPlugin):
    params = [{'name':'Project template',
                'long':'type',
                'short':'t',
                'default':'lib'},

                {'name':'name',
                'long':'name',
                 'default':None}
                ]

    def _create_project_directory(self, project_name):
        if not os.path.exists(project_name):
            os.makedirs(project_name)
            return True
        else:
            print "Project already exists"

    def handle(self, *args, **kwargs):
        project_name = kwargs['name']
        sanitized_project_name = sanitize_name(project_name)
        print "Creating new project %s ..." % sanitized_project_name
        created = self._create_project_directory(sanitized_project_name)
        if not created:
            sys.exit(1)
