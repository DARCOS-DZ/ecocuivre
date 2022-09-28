# Copyright (c) 2022, Ecocuivre and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Transformation(Document):
	def before_submit(self):
		doc = frappe.new_doc('Stock Entry')
		doc.stock_entry_type = 'Material Transfer for Manufacture'
		count = -1
		transformation_dict = self.as_dict()["transformation_items"]
		for item in transformation_dict :
			count += 1
			doc.append("items", {
				"item_code": self.as_dict()["transformation_items"][count]["item"],
				"qty": self.as_dict()["transformation_items"][count]["qty"],
			    "s_warehouse": self.as_dict()["transformation_items"][count]["source_warehouse"],
			    "t_warehouse": self.as_dict()["transformation_items"][count]["transit_warehouse"],
			})

		doc.insert()
		doc.submit()

		self.transfer_for_manufacture_entry = doc.name

		doc = frappe.new_doc('Stock Entry')
		doc.stock_entry_type = 'Manufacture'
		count = -1
		for item in self.as_dict()["transformation_items"] :
			count += 1
			doc.append("items", {
				"item_code": self.as_dict()["transformation_items"][count]["item"],
				"qty": self.as_dict()["transformation_items"][count]["qty"],
			    "s_warehouse": self.as_dict()["transformation_items"][count]["transit_warehouse"],
			})
		doc.append("items", {
			"item_code": self.finished_item,
			"qty": self.qty,
		    "t_warehouse": self.target_warehouse,
			"is_finished_item": True
		})

		doc.insert()
		doc.submit()

		self.manufacture_entry = doc.name

	def on_cancel(self):
		doc = frappe.get_doc('Stock Entry', self.manufacture_entry)
		doc.cancel()

		doc = frappe.get_doc('Stock Entry', self.transfer_for_manufacture_entry)
		doc.cancel()
