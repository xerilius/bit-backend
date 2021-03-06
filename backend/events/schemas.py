from backend import ma
from marshmallow import fields, validate


# This schema is used to validate the badge form data
class EventFormSchema(ma.Schema):
    name = fields.Str(required=True)
    date = fields.DateTime(required=True, format="%Y-%m-%dT%H:%M:%S%z")
    summary = fields.Str(required=True)
    location = fields.Str(required=True, validate=[validate.Length(max=50)])
    presenters = fields.List(fields.Str, required=True)

    class Meta:
        # Fields to show when sending data
        fields = ("name", "date", "summary", "location", "presenters")
        ordered = True


# This schema is used to display the event data
class EventSchema(ma.Schema):
    name = fields.Str(required=True)
    date = fields.Date(required=True)
    summary = fields.Str(required=True)
    location = fields.Str(required=True, validate=[validate.Length(max=50)])
    organization = fields.Nested("OrganizationSchema", only=("id", "name"))
    presenters = fields.Nested("UserSchema", only=("email",), many=True)
    rsvp_list = fields.Nested("UserSchema", only=("email",), many=True)

    class Meta:
        # Fields to show when sending data
        fields = ("name", "date", "summary", "location", "organization", "presenters", "rsvp_list")
        ordered = True


event_form_schema = EventFormSchema()
event_schema = EventSchema()
