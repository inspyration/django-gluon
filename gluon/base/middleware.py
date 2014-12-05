from django.db.models import signals
from django.utils.functional import curry

from .fields import UserField

from . import registration


class GluonMiddleware(object):  # TODO: Register classes and use hooks.
    def process_request(self, request):
        if request.method in ("GET", "HEAD", "OPTION", "TRACE"):
            # this request shouldn't update anything
            # so no signal handler should be attached
            return

        if hasattr(request, "user") and request.user.is_authenticated():
            user = request.user
        else:
            user = None

        update_base_mixin_fields = curry(self._update_base_mixin_fields, user)
        signals.pre_save.connect(update_base_mixin_fields,
                                 dispatch_uid=request,
                                 weak=False)

        delete_base_mixin_fields = curry(self._delete_base_mixin_fields, user)
        signals.pre_delete.connect(delete_base_mixin_fields,
                                   dispatch_uid=request,
                                   weak=False)

    def process_response(self, request, response):
        signals.pre_save.disconnect(dispatch_uid=request)
        return response

    def _update_base_mixin_fields(self, user, sender, instance, created, **kw):
        # update last_modified_by and created_by
        registry = registration.FieldRegistry(UserField)
        if sender in registry:
            for field in registry.get_fields(sender):
                if field.name == "last_modified_by":
                    instance.last_modified_by = user
                if created and field.name == "created_by":
                    instance.created_by = user

    def _delete_base_mixin_fields(self, user, sender, instance, **kw):
        # update last_modified_by and created_by
        registry = registration.FieldRegistry(UserField)
        if sender in registry:
            for field in registry.get_fields(sender):
                if field.name == "deleted_by":
                    instance.deleted_by = user
