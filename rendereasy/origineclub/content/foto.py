# -*- coding: utf-8 -*-
"""Definition of the Foto content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from rendereasy.origineclub import origineclubMessageFactory as _

from rendereasy.origineclub.interfaces import IFoto
from rendereasy.origineclub.config import PROJECTNAME

FotoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.ImageField(
        'arquivo',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Foto"),
        ),
        required=True,
        validators=('isNonEmptyFile'),
        sizes = {'foto' : (1248, 702)}
    ),


    atapi.StringField(
        'legenda',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Legenda"),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

FotoSchema['title'].widget.visible = {"edit": "invisible", "view": "invisible"}
FotoSchema['title'].required = False
FotoSchema['title'].storage = atapi.AnnotationStorage()
FotoSchema['description'].storage = atapi.AnnotationStorage()
FotoSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
FotoSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
FotoSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
FotoSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
FotoSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
FotoSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
FotoSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
FotoSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
FotoSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
FotoSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
FotoSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
FotoSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}


schemata.finalizeATCTSchema(FotoSchema, moveDiscussion=False)


class Foto(base.ATCTContent):
    """Description of the Example Type"""
    implements(IFoto)

    meta_type = "Foto"
    schema = FotoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    arquivo = atapi.ATFieldProperty('arquivo')

    legenda = atapi.ATFieldProperty('legenda')

    def at_post_create_script(self):
        if self.getLegenda():
            self.setTitle(self.getLegenda())
        else:
            self.setTitle(self.id)
        self.reindexObject(idxs=["Title"])


atapi.registerType(Foto, PROJECTNAME)
