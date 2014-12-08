from django.db.models import signals
from django.utils.functional import curry

from base.fields import UserField

from base.registration import FieldRegistry


class GluonSaasMiddleware(object):
    def process_request(self, request):
        if request.method in ("GET", "HEAD", "OPTION", "TRACE"):
            # this request shouldn't update anything
            # so no signal handler should be attached
            return

        if hasattr(request, "user") and request.user.is_authenticated():
            user = request.user
            if hasattr(request, "instance"):
                instance = user.instance
            else:
                instance = None
        else:
            instance = None
            user = None


        update_base_mixin_fields = curry(self._update_base_mixin_fields, user)
        signals.post_save.connect(update_base_mixin_fields,
                                 dispatch_uid=request,
                                 weak=False)

    def process_response(self, request, response):
        signals.post_save.disconnect(dispatch_uid=request)
        return response

    def _update_base_mixin_fields(self, user, sender, instance, created, **kw):
        # update last_modified_by and created_by
        registry = FieldRegistry(UserField)
        if sender in registry:
            for field in registry.get_fields(sender):
                if created and field.name == "owner":
                    instance.owner = user

