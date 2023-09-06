# Copyright (c) 2023, Ideen and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import get_url_to_form
from frappe.desk.notifications import enqueue_create_notification
from frappe.share import add as add_share
from frappe import _
from frappe.desk.doctype.notification_log.notification_log import (
	enqueue_create_notification,
	get_title,
	get_title_html,
)
from frappe.utils import get_fullname
class demp(Document):
	# pass
	def before_save(self):
		print(self.name)
		

	# title = get_title(doctype, doc_name)

		reference_user = get_fullname(frappe.session.user)
		notification_message = _("{0} assigned to {1}  ").format(
			frappe.bold(reference_user), frappe.bold(_(self.contact)))
		
	
		notification_doc = {
			"type": "Assignment",  
			"document_type":"demp",
			"subject":notification_message,
			"document_name":self.name, 
			"from_user":frappe.session.user,
			
		}

		
		enqueue_create_notification("isaluideen@gmail.com", notification_doc)



# @frappe.whitelist()
# def add_notification(contact,docname):
	
	
