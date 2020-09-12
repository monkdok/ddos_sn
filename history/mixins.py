from django.shortcuts import get_object_or_404

from .signals import object_viewed_signal


# class ObjectViewMixin:
#     def dispatch(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#         except self.model.DoesNotExist:
#             instance = None
#
#         if request.user.is_authenticated and instance is not None:
#             # object_viewed_signal.send(instance.__class__, instance=instance, request=request)
#             object_viewed_signal.send(instance.__class__, request=request)
#         return super().dispatch(request, *args, **kwargs)


class ObjectViewMixin:
    def dispatch(self, request, *args, **kwargs):
        object_viewed_signal.send(self.model, request=request)
        return super().dispatch(request, *args, **kwargs)