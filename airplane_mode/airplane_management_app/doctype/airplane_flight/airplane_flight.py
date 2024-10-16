# Copyright (c) 2024, Kibet Sang and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.status='Completed'
	
	def on_cancle(self):
		self.status='Cancelled'
	def update_gate_number(flight, new_gate):
		tickets = frappe.get_all('Ticket', filters={'flight': flight})
		for ticket in tickets:frappe.db.set_value('Ticket', ticket.name, 'gate_number', new_gate)
