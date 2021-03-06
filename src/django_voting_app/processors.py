# django-voting-app - Simple django app to organise votes
# Copyright (C) 2020 Yoann Piétri

# django-voting-app is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# django-voting-app is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with django-voting-app. If not, see <https://www.gnu.org/licenses/>.

"""
Custom processors for django-voting-app
"""

from django.conf import settings


def conf_processor(request):
    """Setting processors.
    This processor let the templates have access to some chosen variables of the settings.
    Args:
        request (HttpRequest): django request object.
    Returns:
        dict: context with the chosen values.
    """
    return {
        "VOTE_NAME": settings.VOTE_NAME,
        "VOTE_LOCAL_LEGALS": settings.VOTE_LOCAL_LEGALS,
    }
