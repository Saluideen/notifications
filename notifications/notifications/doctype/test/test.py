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

class Test(Document):
	# pass
	def on_update(self):
		# add_share(self.doctype, self.name, user='salu@gmail.com', read=1, write=1, submit=0, share=1, everyone=0, notify=0)
		notify_assignment('salu@gmail.com','Test',self.name)


def notify_assignment(shared_by, doctype, doc_name):

	if not (shared_by and doctype and doc_name) :
		return

	from frappe.utils import get_fullname

	title = get_title(doctype, doc_name)

	reference_user = get_fullname(frappe.session.user)
	notification_message = _("{0} shared a document {1} {2} ").format(
		frappe.bold(reference_user), frappe.bold(_(doctype)), get_title_html(title))
	

	notification_doc = {
		"type": "Alert",
		"document_type": doctype,
		"subject": notification_message,
		"document_name": doc_name,
		"from_user": frappe.session.user,
		
	}

	
	enqueue_create_notification(shared_by, notification_doc)