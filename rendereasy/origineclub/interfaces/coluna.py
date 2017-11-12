from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.origineclub import origineclubMessageFactory as _



class IColuna(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    autor = schema.TextLine(
        title=_(u"Autor"),
        required=True,
        description=_(u"Field description"),
    )
#
    foto = schema.Bytes(
        title=_(u"Foto"),
        required=True,
        description=_(u"Field description"),
    )
#
