from veva.models import user_register
from admin_app.models import add_product
from user_app.models import Cart

def cart_item_count(request):
    cart_count = 0
    if request.session.get('uid'):
        try:
            user = user_register.objects.get(id=request.session['uid'])
            cart_count = Cart.objects.filter(user=user).count()
        except user_register.DoesNotExist:
            pass
    return {'cart_count': cart_count}