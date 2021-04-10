from app import call_filter, app

"""
setup_database(app)
"""
call_filter(app)
print('this is main')

if __name__ == '__main__':
    app.run(debug=True)