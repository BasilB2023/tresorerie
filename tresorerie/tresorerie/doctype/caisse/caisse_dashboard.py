from frappe import _


def get_data():
	return {
		"heatmap": True,
		"heatmap_message": _("This is based on the Time Sheets created against this project"),
		"fieldname": "caisse",
		"transactions": [
			{
				"label": _("Caisse"),
				"items": ["Caisse Initialisation"],
			},
		],
	}
