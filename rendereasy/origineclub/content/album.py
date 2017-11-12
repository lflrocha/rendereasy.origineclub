# -*- coding: utf-8 -*-
"""Definition of the Album content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from rendereasy.origineclub.interfaces import IAlbum
from rendereasy.origineclub.config import PROJECTNAME

AlbumSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

AlbumSchema['title'].widget.label = _(u"Nome do Álbum")
AlbumSchema['title'].storage = atapi.AnnotationStorage()
AlbumSchema['description'].storage = atapi.AnnotationStorage()
AlbumSchema['description'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['effectiveDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['subject'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['relatedItems'].widget.visible = {"edit": "invisible", "view": "invisible"}
AlbumSchema['nextPreviousEnabled'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(
    AlbumSchema,
    folderish=True,
    moveDiscussion=False
)


class Album(folder.ATFolder):
    """Description of the Example Type"""
    implements(IAlbum)

    meta_type = "Album"
    schema = AlbumSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    def getFotos(self):
        pc = getToolByName(self, 'portal_catalog')
        path = join(self.getPhysicalPath(), '/')
        fotos = pc.searchResults(meta_type='Foto',path=path)
        return fotos

    def getAutomator(self):
        fotos = self.listFolderContents()
        novoProjeto =  DateTime().strftime("%Y%m%d%H%M%S") + '_' + self.meta_type

        aux = 'var ext_cliente = "origine";\n'
        aux = aux + 'var ext_novoProjeto = "%s";\n' % novoProjeto
        aux = aux + 'var ext_telas = [\n'
        for foto in fotos:
            arquivo = foto.getId()
            legenda = foto.getLegenda()
            aux = aux + '{\n'
            aux = aux + 'name: "fotos",\n'
            aux = aux + 'tempo: 10,\n'
            aux = aux + 'legenda: "%s",\n' % legenda
            aux = aux + 'foto: "%s",\n' % arquivo
            aux = aux + 'bg: "blur"\n'
            aux = aux + '}, \n'
        aux = aux[:-3] + '\n]\n'

        return aux



atapi.registerType(Album, PROJECTNAME)
