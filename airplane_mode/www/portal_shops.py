import frappe

def get_context(context):
    """Get the context for the available shops portal."""
    context.available_shops = frappe.get_all(
        'Shop', 
        filters={'is_leased': 0}, 
        fields=['shop_name', 'shop_number', 'area', 'airport']
    )
