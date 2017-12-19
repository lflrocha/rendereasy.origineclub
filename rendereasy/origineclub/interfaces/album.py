from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.origineclub import origineclubMessageFactory as _



class IAlbum(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    trilha = schema.Bytes(
        title=_(u"Trilha"),
        required=True,
        description=_(u"Field description"),
    )
#
