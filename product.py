from flask import Blueprint, render_template
product=Blueprint('product',__name__)

@product.route('/product')
def productpage():
    return render_template("product.html")