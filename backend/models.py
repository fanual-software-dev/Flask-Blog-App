from mongoengine import Document, StringField, DateTimeField,IntField

class BlogSchema(Document):
    title = StringField(required = True)
    main = StringField(required = True)
    image = StringField(required = True)
    numberOfLikes = IntField(required = True)
    createdAt = DateTimeField(required=True)