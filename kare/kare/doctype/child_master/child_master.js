// Copyright (c) 2020, EpochConsulting and contributors
// For license information, please see license.txt

frappe.ui.form.on('Child Master', {
	refresh: function(frm) {
		 cur_frm.add_custom_button(__('Case'), function() {
			frappe.model.open_mapped_doc({
			    method: "kare.kare.doctype.child_master.child_master.make_case",
			    frm: cur_frm
			})
		}, __("Make"))
		 cur_frm.add_custom_button(__('Couselling'), function() {
			frappe.model.open_mapped_doc({
			    method: "kare.kare.doctype.child_master.child_master.make_counselling",
			    frm: cur_frm
			})
		}, __("Make"))
	}
});
