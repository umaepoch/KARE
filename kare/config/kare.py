from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
                {
                        "label": _("KARE Document"),
                        "icon": "fa fa-star",
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Child Master",
                                        "description": _("Database of potential customers."),
                                        "onboard": 1,
                                },
                                {
                                        "type": "doctype",
                                        "name": "Case",
                                        "description": _("Database of potential customers."),
                                        "onboard": 1,
                                },
                                {
                                        "type": "doctype",
                                        "name": "Counselling",
                                        "description": _("Database of potential customers."),
                                        "onboard": 1,
                                }
			]
		}
	]

