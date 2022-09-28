// Copyright (c) 2022, Ecocuivre and contributors
// For license information, please see license.txt

frappe.ui.form.on('Transformation', {
	// refresh: function(frm) {

	// }

  refresh(frm) {
    if (frm.doc.docstatus === 0) frm.set_value('manufacture_entry', '');
    if (frm.doc.docstatus === 0) frm.set_value('transfer_for_manufacture_entry', '');
  }
});
