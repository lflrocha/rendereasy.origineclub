"""Definition of the Evento content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from rendereasy.origineclub.interfaces import IEvento
from rendereasy.origineclub.config import PROJECTNAME

EventoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

EventoSchema['title'].storage = atapi.AnnotationStorage()
EventoSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(EventoSchema, moveDiscussion=False)


class Evento(base.ATCTContent):
    """Description of the Example Type"""
    implements(IEvento)

    meta_type = "Evento"
    schema = EventoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Evento, PROJECTNAME)
