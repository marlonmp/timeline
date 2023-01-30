from rest_framework import generics


class ListFieldViewMixin:

    def get_queryset(self):
        field_value = self.kwargs.get(self.lookup_field)

        attrs = { self.lookup_field: field_value }

        queryset = super().get_queryset()

        object = generics.get_object_or_404(queryset, **attrs)

        return getattr(object, self.list_field)
