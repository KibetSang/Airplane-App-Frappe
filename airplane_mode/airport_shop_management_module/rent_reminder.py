import frappe
from frappe.utils import today, add_days

def send_rent_reminders():
    """Send rent reminders if enabled in settings."""
    # Check if rent reminders are enabled
    shop_settings = frappe.get_single('Shop Settings')
    if not shop_settings.enable_rent_reminders:
        return  # Do nothing if reminders are disabled

    # Fetch tenants whose rent is due today
    tenants_due = frappe.get_all('RentPayment', filters={'due_date': ['<=', today()]}, fields=['tenant', 'shop'])

    for tenant in tenants_due:
        tenant_info = frappe.get_doc('Tenant', tenant.tenant)
        shop_info = frappe.get_doc('Shop', tenant.shop)

        # Send email
        frappe.sendmail(
            recipients=tenant_info.email,
            subject="Rent Reminder for Shop {}".format(shop_info.shop_number),
            message="""Dear {tenant_name}, your rent for Shop {shop_number} is due. Please make payment."""
        )
