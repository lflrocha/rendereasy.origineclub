# -*- coding: utf-8 -*-
"""Definition of the Coluna content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from rendereasy.origineclub import origineclubMessageFactory as _

from rendereasy.origineclub.interfaces import IColuna
from rendereasy.origineclub.config import PROJECTNAME

ColunaSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'autor',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Autor"),
        ),
        required=True,
    ),

    atapi.ImageField(
        'foto',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Foto"),
        ),
        required=True,
        validators=('isNonEmptyFile'),
    ),



))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

ColunaSchema['title'].storage = atapi.AnnotationStorage()
ColunaSchema['description'].storage = atapi.AnnotationStorage()
ColunaSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
ColunaSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
ColunaSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
ColunaSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
ColunaSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
ColunaSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
ColunaSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
ColunaSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
ColunaSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
ColunaSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
ColunaSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
ColunaSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(ColunaSchema, moveDiscussion=False)


class Coluna(base.ATCTContent):
    """Description of the Example Type"""
    implements(IColuna)

    meta_type = "Coluna"
    schema = ColunaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    autor = atapi.ATFieldProperty('autor')

    foto = atapi.ATFieldProperty('foto')

    def getAutomator(self):
        novoProjeto =  DateTime().strftime("%Y%m%d%H%M%S") + '_' + self.meta_type

        aux = 'var ext_cliente = "origine";\n'
        aux = aux + 'var ext_novoProjeto = "%s";\n' % novoProjeto
        aux = aux + 'var ext_telas = [{\n'
        aux = aux + 'name: "coluna",\n'
        aux = aux + 'tempo: 15,\n'
        aux = aux + 'titulo: "%s",\n' % self.Title()
        aux = aux + 'autor: "%s",\n' % self.getAutor()
        aux = aux + 'foto: "%s",\n' % self.getFoto()
        aux = aux + '}]; \n'

        return aux


atapi.registerType(Coluna, PROJECTNAME)
