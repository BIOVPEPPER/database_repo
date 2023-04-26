
from flask import Blueprint, render_template, request, url_for,flash, g
from app import db


main = Blueprint('main', __name__)

def sql_query(keyword):
    if keyword == "*":
        query = "SELECT * from Products LIMIT 10"
    else:
        query = "select * from Products where ProductName like '%{keyword}%' limit 10".format(keyword=keyword)
    #I am not sure whether this is the way to execute the query with the SQLalchemy, but you know what I mean.
    data = db.engine.execute(query)
    return data

@main.route('/',methods=['GET', 'POST'])
def products():
    if request.method== 'POST':
        keyword= request.form['keyword']
        result = sql_query(keyword)
        return render_template("products.html", data = result)
    return render_template("products.html",data = sql_query("*"))


@main.route('/mywishlist')
def mywishlist():
    return render_template("mywishlist.html", wishlist=True)

@main.route('/myorders')
def myorders():
    return render_template("myorders.html", orders=True)


