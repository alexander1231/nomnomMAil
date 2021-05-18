import poplib, os
import uuid
from email.parser import Parser
from application.models import Email, Attachment

pop3_server_domain = 'pop.secureserver.net'
pop3_server_conn = None

'''
This method will connect to the global pop3 server
and login with the provided user email and password.
'''
def connect_pop3_server(user_email, user_password):
    global pop3_server_conn

    if (pop3_server_conn is None):
        print('********************************* start connect_pop3_server *********************************')
        pop3_server_conn = poplib.POP3(pop3_server_domain)
        # pop3_server_conn.set_debuglevel(1)

        pop3_server_conn.user(user_email)
        pop3_server_conn.pass_(user_password)

    return pop3_server_conn

'''
Close the pop3 server connection and release the connection object.
'''
def close_pop3_server_connection():
    global pop3_server_conn
    if pop3_server_conn != None:
        pop3_server_conn.quit()
        pop3_server_conn = None

'''
Get email messages status of the given user.
'''
def get_user_email_status(user_email, user_password):

    connect_pop3_server(user_email, user_password)

    (messageCount, totalMessageSize) = pop3_server_conn.stat()
    print(messageCount)

    return messageCount

'''
Get email by the provided email account and email index number.
'''
def get_email_by_index(user_email, user_password, email_index):

    connect_pop3_server(user_email, user_password)

    ### header
    resp_message, lines, octets = pop3_server_conn.top(email_index, 0)
    header_content= b'\n'.join(lines).decode('utf-8')

    ### body
    (resp_message, lines, octets) = pop3_server_conn.retr(email_index)
    msg_content = b'\n'.join(lines).decode('utf-8')
    body_content = msg_content.replace(header_content, '')

    email_uuid = generate_uuid()
    save_db = Email(user_email, email_uuid, header_content, body_content).save()
    get_attachments(msg_content, email_uuid)

    return save_db

def get_attachments(msg, email_uuid):
    # TO DO: Upload file to s3 and digital ocean spaces
    parts = Parser().parsestr(msg)

    for part in parts.walk():
        content_type = part.get_content_type()
        if content_type.startswith('image') or content_type.startswith('application'):
            attach_file_info_string = part.get('Content-Disposition')
            prefix = 'filename="'
            pos = attach_file_info_string.find(prefix)
            attach_file_name = attach_file_info_string[pos + len(prefix): len(attach_file_info_string) - 1]
            print(attach_file_name)

            attach_file_data = part.get_payload(decode=True)
            current_path = os.path.dirname(os.path.abspath(__file__))
            attach_file_path = current_path + '/attachments/' + attach_file_name
            print(attach_file_path)
            with open(attach_file_path,'wb') as f:
                f.write(attach_file_data)

            save_db = Attachment(generate_uuid(), email_uuid, attach_file_path, attach_file_name).save()


def generate_uuid():
    return uuid.uuid4().hex

