from flask import Flask
from flask import render_template , request, redirect, url_for
from flask import current_app as app


@app.route('/admin_panel')
def admin_panel():
    return render_template('admin/admin_panel.html')

@app.route('/admin/pyq')
def admin_pyq():
    return render_template("admin/pyq.html")
