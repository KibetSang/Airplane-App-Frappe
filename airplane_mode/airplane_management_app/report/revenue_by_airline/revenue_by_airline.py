# # Copyright (c) 2024, Kibet Sang and contributors
# # For license information, please see license.txt

# import frappe

# def get_cols():
# 	# Define the columns for the report
# 	return [
# 		{
# 			"fieldname": "airline",
# 			"label": "Airline",
# 			"fieldtype": "Link",
# 			"options": "Airline",
# 			"width": 110
# 		},
# 		{
# 			"fieldname": "revenue",
# 			"label": "Revenue",
# 			"fieldtype": "Currency",
# 			"width": 110
# 		}
# 	]

# def get_data():
# 	# Fetch all airlines
# 	airlines = frappe.get_all("Airline", fields=["name"])
# 	data = []

# 	# Loop through each airline and calculate its total revenue
# 	for airline in airlines:
# 		# Calculate the total revenue for each airline, including add-ons
# 		revenue = frappe.db.sql("""
# 			SELECT SUM(t.total_amount + IFNULL(ai.total_addon_amount, 0)) AS Total_Revenue
# 			FROM `tabAirplane Ticket` t
# 			JOIN `tabFlight` f ON t.flight = f.name
# 			JOIN `tabAirplane` a ON f.airplane = a.name
# 			LEFT JOIN (
# 				SELECT parent, SUM(amount) AS total_addon_amount
# 				FROM `tabAirplane Ticket Add-on Item`
# 				GROUP BY parent
# 			) ai ON t.name = ai.parent
# 			WHERE a.airline = %s
# 		""", (airline.name), as_list=True)[0][0] or 0.0

# 		# Append the airline name and its calculated revenue to the data
# 		data.append([airline.name, revenue])
# 	return data

# def get_chart_data(data):
# 	# Prepare chart data using airline names as labels and revenue as values
# 	labels = [row[0] for row in data]
# 	values = [row[1] for row in data]

# 	chart = {
# 		"data": {
# 			"labels": labels,
# 			"datasets": [
# 				{
# 					"name": "Revenue",
# 					"values": values
# 				}
# 			]
# 		},
# 		"type": "donut"
# 	}
# 	return chart

# def execute(filters=None):
# 	# Get the columns and data
# 	columns = get_cols()
# 	data = get_data()

# 	# Generate chart data based on the data fetched
# 	chart = get_chart_data(data)

# 	# Calculate total revenue across all airlines
# 	total_revenue = sum(row[1] for row in data)
	
# 	# Append a summary row for total revenue
# 	data.append(["Total Revenue", total_revenue])

# 	# Summary for report footer
# 	summary = [
# 		{'label': 'Total Revenue', 'value': frappe.format_value(total_revenue, 'Currency')}
# 	]

# 	# Return the columns, data, and chart, along with the summary
# 	return columns, data, None, chart, summary
import frappe

def execute(filters=None):
	# Define the columns for the report
	columns = [
		{
			"fieldname": "airline",
			"label": "Airline",
			"fieldtype": "Link",
			"options": "Airline",
		},
		{
			"fieldname": "total_revenue",
			"label": "Total Revenue",
			"fieldtype": "Currency",
		}
	]

	# Fetch total revenue per airline
	data = frappe.db.sql("""
		SELECT a.airline, SUM(t.total_amount) AS total_revenue
		FROM `tabAirplane Ticket` t
		JOIN `tabFlight` f ON t.flight = f.name
		JOIN `tabAirplane` a ON f.airplane = a.name
		GROUP BY a.airline
		ORDER BY total_revenue DESC
	""", as_dict=True)

	# Prepare chart data
	chart = {
		"data": {
			"labels": [row["airline"] for row in data],
			"datasets": [{"values": [row["total_revenue"] for row in data]}],
		},
		"type": "donut",
	}

	# Return the columns, data, and chart
	return columns, data, None, chart
