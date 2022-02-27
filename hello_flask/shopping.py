import sys
from flask import render_template, Blueprint, request, url_for, g, session, redirect, flash, jsonify
from api import create, read as getter, update, delete as deler, db_conn
from auth import login_required

col = 'shopping'
bp = Blueprint(col, __name__, url_prefix='/shopping')

# adding to the shopping list.
@bp.route('/list',methods=['GET','POST'])
@login_required
def shop_list():
    items = getter.get_one(col,{'user':g.user['username']})['items'] if getter.get_one(col,{'user':g.user['username']}) else []
    if request.method == 'POST':
        # items = []
        item = request.form['item']
        items.append(item)
        error = None

        if not item: error = "invalid item"

        if error == None:
            item_dict = {
                'user': g.user['username'],
                'items': items
            }
            try:
                if getter.get_one(col,{'user': g.user['username']}) == None:
                    x = create.create(item_dict,col)
                else:
                    x = update.update(col,{'user': g.user['username']},{'$set':{'items': items}})
            except:
                error = "invalid list"
            return jsonify(items)
        print(error,file=sys.stderr)

    # if request.method == 'GET':
    #     return jsonify(items)

    return render_template('/shopping/list.html',items=items)
