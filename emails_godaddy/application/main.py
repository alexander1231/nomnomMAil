from flask import request, jsonify
from flask import current_app as app
from application import pop3 as pop


@app.route("/autentication", methods=['POST'])
def autentication():
    if request.method == 'POST':
        response = {"response": "Unauthorized"}
        data = request.get_json()

        if data is not None and 'username' in data and 'password' in data:
            autentication = get_messages(data['username'], data['password'])
            print(autentication)
            return jsonify({"response": "OK"}), 200
        else:
            return jsonify(response), 401

def get_messages(username, password):
    try:
        print('QTY EMAILS:')
        messageCount = pop.get_user_email_status(username, password)

        # TO DO: get current index from db
        print('GET EMAILS:')
        get_message(username, password, 1, messageCount)
        return 'Autenticated'
    except:
        # TO DO: save current index from db
        pop.close_pop3_server_connection()
        return 'Error 500'


def get_message(username, password, index, limit):
    if index <= limit:
        save_db = pop.get_email_by_index(username, password, index)

        if save_db:
            print('Email {} saved.'.format(index))
            index = index + 1
            get_message(username, password, index, limit)
        else:
            print('Error with email {}'.format(index))
    else:
        pop.close_pop3_server_connection()
        print('Completed successfully')

