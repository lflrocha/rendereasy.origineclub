from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from rendereasy.origineclub import origineclubMessageFactory as _



class ITexto(Interface):
    """Description of the Example Type"""

    # -*- schema definition goes here -*-
    text = schema.Text(
        title=_(u"Texto"),
        required=True,
        description=_(u"Field description"),
    )
#
    tempo = schema.Int(
        title=_(u"Tempo"),
        required=False,
        description=_(u"Field description"),
    )
#
