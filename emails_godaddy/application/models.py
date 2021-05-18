from application import db

class Email(db.Model):
    __tablename__ = 't_emails'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(32), unique=True, nullable=False)
    username = db.Column(db.String(120), index=True, nullable=False)
    email_header = db.Column(db.Text, nullable=False)
    email_body = db.Column(db.Text(4294000000), nullable=False)
    timestamp_created = db.Column(db.DateTime, server_default=db.func.now())
    timestamp_modified = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, uuid, username, email_header, email_body):
        self.uuid = uuid
        self.username = username
        self.email_header = email_header
        self.email_body = email_body

    def serialize(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'username': self.username,
            'email_header': self.email_header,
            'email_body': self.email_body,
            'timestamp_created': self.timestamp_created,
            'timestamp_modified': self.timestamp_modified
        }

    def save(self):
        try:
            data = Email(self.username, self.uuid, self.email_header, self.email_body)
            db.session.add(data)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def __repr__(self):
        return '<Email id={} uuid={} username={}>'.format(self.id, self.uuid, self.username)


class Attachment(db.Model):
    __tablename__ = 't_attachments'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(32), unique=True, nullable=False)
    email_uuid = db.Column(db.String(32), db.ForeignKey('t_emails.uuid'))
    path = db.Column(db.String(250))
    name = db.Column(db.String(120), nullable=False)
    timestamp_created = db.Column(db.DateTime, server_default=db.func.now())
    timestamp_modified = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, uuid, email_uuid, path, name):
        self.uuid = uuid
        self.email_uuid = email_uuid
        self.path = path
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'uuid': self.uuid,
            'email_uuid': self.email_uuid,
            'path': self.path,
            'name': self.name,
            'timestamp_created': self.timestamp_created,
            'timestamp_modified': self.timestamp_modified
        }

    def save(self):
        try:
            data = Attachment(self.uuid, self.email_uuid, self.path, self.name)
            db.session.add(data)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def __repr__(self):
        return '<Attachment id={} uuid={} email_uuid={} name={} path={}>'.format(self.id, self.uuid, self.email_uuid, self.name, self.path)

