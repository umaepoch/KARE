# -*- coding: utf-8 -*-
# Copyright (c) 2020, EpochConsulting and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.utils import cstr, flt, getdate, comma_and, cint, nowdate, add_days
import json
import datetime
import time

class ChildMaster(Document):
	pass

@frappe.whitelist()
def make_case(frm, target_doc=None, ignore_permissions=False):
	def set_missing_values(frm, target):
		target.name_of_child = frm.name_of_child
		target.date_of_admission = frm.date_of_admission
		target.caregiver_code = frm.caregiver_code
		target.name_of_caregiver = frm.name_of_caregiver
		target.sex = frm.sex
		target.date_of_birth = frm.date_of_birth
		target.case_status = frm.case_status
		target.aadhar_card_no = frm.aadhar_card_no
		target.is_pos = 0
		target.ignore_pricing_rule = 1
		target.run_method("set_missing_values")
		target.run_method("set_po_nos")
		target.run_method("calculate_taxes_and_totals")
	def postprocess(frm, target):
		set_missing_values(frm, target)
	doclist = get_mapped_doc("Child Master", frm, {
		"Child Master": {
			"doctype": "Case",
			"field_map": {
				"refference_doc":frm
				
			},
			"validation": {
				"docstatus": ["=", 0]
			}
		}
	}, target_doc,postprocess, ignore_permissions=ignore_permissions)
	return doclist
@frappe.whitelist()
def make_counselling(frm, target_doc=None, ignore_permissions=False):
	def set_missing_values(frm, target):
		target.name_of_child = frm.name_of_child
		target.date_of_admission = frm.date_of_admission
		target.caregiver_code = frm.caregiver_code
		target.name_of_caregiver = frm.name_of_caregiver
		target.sex = frm.sex
		target.date_of_birth = frm.date_of_birth
		target.aadhar_card_no = frm.aadhar_card_no
		#target.is_pos = 0
		#target.ignore_pricing_rule = 1
		#target.run_method("set_missing_values")
		#target.run_method("set_po_nos")
		#target.run_method("calculate_taxes_and_totals")
	def postprocess(frm, target):
		set_missing_values(frm, target)
	doclist = get_mapped_doc("Child Master", frm, {
		"Child Master": {
			"doctype": "Counselling",
			"field_map": {
				"refference_doc":frm
				
			},
			"validation": {
				"docstatus": ["=", 0]
			}
		}
	}, target_doc,postprocess, ignore_permissions=ignore_permissions)
	return doclist
