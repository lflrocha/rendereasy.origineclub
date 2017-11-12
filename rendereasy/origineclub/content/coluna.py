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

from DateTime.DateTime import *
from Products.CMFPlone.utils import getToolByName
from string import join

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

    def getDados(self):
        novoProjeto =  DateTime().strftime("%Y%m%d%H%M%S") + '_' + self.meta_type
        filename = self.getFilename('foto')


        aux = 'var ext_cliente = "origine";\n'
        aux = aux + 'var ext_novoProjeto = "%s";\n' % novoProjeto
        aux = aux + 'var ext_telas = [\n'

        aux = aux + '{\n'
        aux = aux + 'name: "vinheta",\n'
        aux = aux + 'texto: "Colunistas Origine",\n'
        aux = aux + '},\n'
        aux = aux + '{\n'
        aux = aux + 'name: "coluna",\n'
        aux = aux + 'tempo: 10,\n'
        aux = aux + 'titulo: "%s",\n' % self.Title()
        aux = aux + 'autor: "%s",\n' % self.getAutor()
        aux = aux + 'foto: "%s",\n' % filename
        aux = aux + '},\n'
        aux = aux + '{\n'
        aux = aux + 'name: "assinatura",\n'
        aux = aux + 'texto: "originegroup.com.br"\n'
        aux = aux + '}\n'        
        aux = aux + '];\n'
        aux = aux + 'var arquivos = [("%s/at_download/foto/", "%s")];' % (self.absolute_url(), filename)


        return aux


atapi.registerType(Coluna, PROJECTNAME)
