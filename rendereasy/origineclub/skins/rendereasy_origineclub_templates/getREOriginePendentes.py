## Script (Python) "getNbrInfowebItems"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
solicitacoes = context.portal_catalog.searchResults(meta_type=['Twitter', 'Texto', 'Santinho', 'Album'], sort_on="created")

aux = []
for s in solicitacoes:
    aux.append( { 'tipo': s.Type, 'endereco': s.getURL(), 'titulo': s.Title }  )

return aux
