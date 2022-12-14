from django.urls import path
from . import views
from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    checkout,
    update_transaction_records,
    success
)

urlpatterns = [
    path('add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    path('order-summary/$', order_details, name="order_summary"),
    path('success/$', success, name='purchase_success'),
    path('item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    path('checkout/$', checkout, name='checkout'),
    path('update-transaction/(?P<token>[-\w]+)/$', update_transaction_records,
        name='update_records')
]