"""Definition of the Texto content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from rendereasy.origineclub import origineclubMessageFactory as _

from rendereasy.origineclub.interfaces import ITexto
from rendereasy.origineclub.config import PROJECTNAME

TextoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.TextField(
        'text',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Texto"),
        ),
        required=True,
    ),


    atapi.IntegerField(
        'tempo',
        storage=atapi.AnnotationStorage(),
        widget=atapi.IntegerWidget(
            label=_(u"Tempo"),
            description=_(u"Field description"),
        ),
        validators=('isInt'),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

TextoSchema['title'].storage = atapi.AnnotationStorage()
TextoSchema['description'].storage = atapi.AnnotationStorage()
TextoSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
TextoSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}


schemata.finalizeATCTSchema(TextoSchema, moveDiscussion=False)


class Texto(base.ATCTContent):
    """Description of the Example Type"""
    implements(ITexto)

    meta_type = "Texto"
    schema = TextoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    texto = atapi.ATFieldProperty('text')

    tempo = atapi.ATFieldProperty('tempo')


atapi.registerType(Texto, PROJECTNAME)
