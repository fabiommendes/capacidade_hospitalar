from django import forms
from material.frontend.views import CreateModelView, ListModelView, UpdateModelView

__all__ = ["NotifierListModelView", "NotifierUpdateModelView", "NotifierCreateModelView"]


class NotifierCreateOrUpdateMixin:
    def form_valid(self, form: forms.ModelForm, *args, **kwargs):
        save_fn = form.save
        user = self.request.user

        def save():
            obj = save_fn(commit=False)
            obj.notifier = user
            obj.save()
            form.save_m2m()
            return obj

        form.save = save
        return super().form_valid(form, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        user = self.request.user
        unities = user.healthcare_units.all()

        if len(unities) == 1:
            self.prepare_form_for_single_unit(form, unities[0])
        field: forms.Field = form.fields["unit"]
        field.queryset = unities
        return form

    def prepare_form_for_single_unit(self, form, unit):
        form.initial["unit"] = unit
        field: forms.Field = form.fields["unit"]
        field.disabled = True

        capacity = unit.capacity_notifications.order_by("date").last()
        if capacity:
            for k, v in capacity.capacities.items():
                form.initial.setdefault(k, v)


class NotifierCreateModelView(NotifierCreateOrUpdateMixin, CreateModelView):
    pass


class NotifierUpdateModelView(NotifierCreateOrUpdateMixin, UpdateModelView):
    pass


class NotifierListModelView(ListModelView):
    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(notifier=user)
