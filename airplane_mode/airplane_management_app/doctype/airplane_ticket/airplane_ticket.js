// Copyright (c) 2024, Kibet Sang and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on('Airplane Ticket Add-on Item', {
    item: function(frm, cdt, cdn) {
        var d = locals[cdt][cdn];
        $.each(frm.doc.add_ons, function(i, row) {
            if (row.item === d.item && row.name != d.name) {
               frappe.model.remove_from_locals(cdt, cdn);
               frm.refresh_field('add_ons');
               return false;
            }
        });
    }
});

frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {
        frm.add_custom_button(__('Assign Seat'), function() {
            let seat_dialog = new frappe.ui.Dialog({
                title: 'Enter Seat Number',
                fields: [
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ],
                primary_action_label: 'Assign Seat',
                primary_action(values) {
                    frm.set_value('seat', values.seat_number);
                    seat_dialog.hide();
                    frm.save();  
                }
            });
            // Show the dialog
            seat_dialog.show();
        });
    }
});
