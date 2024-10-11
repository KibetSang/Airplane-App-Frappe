// Copyright (c) 2024, Kibet Sang and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airline", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Airline', {
    refresh(frm) {
       const airline_website = frm.doc.website;
       frm.add_web_link(airline_website, "View in Website");
    }
   })