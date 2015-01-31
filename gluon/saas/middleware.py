from django.db.models import signals
from django.utils.functional import curry

from .fields import SubscriptionField
from .views import inject_subscription

from base.registration import FieldRegistry


class GluonSaasMiddleware(object):
    def process_request(self, request):
        if request.method in ("GET", "HEAD", "OPTION", "TRACE"):
            # this request shouldn't update anything
            # so no signal handler should be attached
            return

        if hasattr(request, "user") and request.user.is_authenticated():
            subscription = request.user.profile.subscription
        else:
            subscription = None

        update_base_mixin_fields = curry(self._update_base_mixin_fields,
                                         subscription)
        inject_subscription.connect(update_base_mixin_fields,
                                    dispatch_uid="plop",
                                    weak=False)

    def process_response(self, request, response):
        inject_subscription.disconnect(dispatch_uid=request)
        return response

    def _update_base_mixin_fields(self, subscription, sender, instance, **kw):
        # update subscription field
        registry = FieldRegistry(SubscriptionField)
        if sender in registry:
            for field in registry.get_fields(sender):
                if field.name == "subscription":
                    instance.subscription = subscription

