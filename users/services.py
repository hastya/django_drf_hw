from config.settings import STRIPE_SECRET_KEY
import stripe

stripe.api_key = STRIPE_SECRET_KEY


def create_stripe_price(payment):
    stripe_product = stripe.Product.create(name=payment.paid_course.name)
    stripe_price = stripe.Price.create(
        currency='rub',
        unit_amount=int(payment.amount_payment) * 100,
        product_data={'name': stripe_product['name']},
    )
    return stripe_price['id']


def create_stripe_session(stripe_price_id):
    stripe_session = stripe.checkout.Session.create(
        line_items=[{'price': stripe_price_id, 'quantity': 1}],
        mode='payment',
        success_url='https://example.com/success',
    )
    return stripe_session['url'], stripe_session['id']
