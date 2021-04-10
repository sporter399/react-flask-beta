from app import call_filter, app

"""
setup_database(app)
"""
call_filter(app)

if __name__ == '__main__':
    app.run(debug=True)