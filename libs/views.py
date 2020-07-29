from django.urls import reverse
from django.views.generic import DetailView, ListView
from .models import *


class LibsListView(ListView):
    model = t_case
    queryset = t_case.objects.order_by('id').all()

    def render_to_response(self, context, **response_kwargs):
        # Shim to affect the CMS Toolbar only
        if self.request.toolbar:
            menu = self.request.toolbar.get_or_create_menu(
                'staff-list-menu', 'Leadership')
            menu.add_sideframe_item(u'Seniority List', url=reverse(
                'admin:staff_seniority_changelist'))
            menu.add_modal_item('Add new Seniority', url="%s" %
                                (reverse('admin:staff_seniority_add'), ))
            menu.add_break()
            menu.add_sideframe_item(u'Staff List', url=reverse(
                'admin:staff_staffmember_changelist'))
            menu.add_modal_item('Add new Staff Member', url="%s" % (
                reverse('admin:staff_staffmember_add'), ))

        return super(LibsListView, self).render_to_response(context, **response_kwargs)
