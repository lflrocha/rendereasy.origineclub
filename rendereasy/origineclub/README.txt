Introduction
============

This is a full-blown functional test. The emphasis here is on testing what
the user may input and see, and the system is largely tested as a black box.
We use PloneTestCase to set up this test as well, so we have a full Plone site
to play with. We *can* inspect the state of the portal, e.g. using 
self.portal and self.folder, but it is often frowned upon since you are not
treating the system as a black box. Also, if you, for example, log in or set
roles using calls like self.setRoles(), these are not reflected in the test
browser, which runs as a separate session.

Being a doctest, we can tell a story here.

First, we must perform some setup. We use the testbrowser that is shipped
with Five, as this provides proper Zope 2 integration. Most of the 
documentation, though, is in the underlying zope.testbrower package.

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()

The following is useful when writing and debugging testbrowser tests. It lets
us see all error messages in the error_log.

    >>> self.portal.error_log._ignored_exceptions = ()

With that in place, we can go to the portal front page and log in. We will
do this using the default user from PloneTestCase:

    >>> from Products.PloneTestCase.setup import portal_owner, default_password

Because add-on themes or products may remove or hide the login portlet, this test will use the login form that comes with plone.  

    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()

Here, we set the value of the fields on the login form and then simulate a
submit click.  We then ensure that we get the friendly logged-in message:

    >>> "You are now logged in" in browser.contents
    True

Finally, let's return to the front page of our site before continuing

    >>> browser.open(portal_url)

-*- extra stuff goes here -*-
The Texto content type
===============================

In this section we are tesing the Texto content type by performing
basic operations like adding, updadating and deleting Texto content
items.

Adding a new Texto content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Texto' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Texto').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Texto' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Texto Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Texto' content item to the portal.

Updating an existing Texto content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Texto Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Texto Sample' in browser.contents
    True

Removing a/an Texto content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Texto
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Texto Sample' in browser.contents
    True

Now we are going to delete the 'New Texto Sample' object. First we
go to the contents tab and select the 'New Texto Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Texto Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Texto
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Texto Sample' in browser.contents
    False

Adding a new Texto content item as contributor
------------------------------------------------

Not only site managers are allowed to add Texto content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Texto' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Texto').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Texto' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Texto Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Texto content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Evento content type
===============================

In this section we are tesing the Evento content type by performing
basic operations like adding, updadating and deleting Evento content
items.

Adding a new Evento content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Evento' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Evento').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Evento' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Evento Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Evento' content item to the portal.

Updating an existing Evento content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Evento Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Evento Sample' in browser.contents
    True

Removing a/an Evento content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Evento
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Evento Sample' in browser.contents
    True

Now we are going to delete the 'New Evento Sample' object. First we
go to the contents tab and select the 'New Evento Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Evento Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Evento
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Evento Sample' in browser.contents
    False

Adding a new Evento content item as contributor
------------------------------------------------

Not only site managers are allowed to add Evento content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Evento' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Evento').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Evento' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Evento Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Evento content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Vinheta content type
===============================

In this section we are tesing the Vinheta content type by performing
basic operations like adding, updadating and deleting Vinheta content
items.

Adding a new Vinheta content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Vinheta' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Vinheta').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Vinheta' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Vinheta Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Vinheta' content item to the portal.

Updating an existing Vinheta content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Vinheta Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Vinheta Sample' in browser.contents
    True

Removing a/an Vinheta content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Vinheta
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Vinheta Sample' in browser.contents
    True

Now we are going to delete the 'New Vinheta Sample' object. First we
go to the contents tab and select the 'New Vinheta Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Vinheta Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Vinheta
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Vinheta Sample' in browser.contents
    False

Adding a new Vinheta content item as contributor
------------------------------------------------

Not only site managers are allowed to add Vinheta content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Vinheta' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Vinheta').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Vinheta' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Vinheta Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Vinheta content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The PerguntaResposta content type
===============================

In this section we are tesing the PerguntaResposta content type by performing
basic operations like adding, updadating and deleting PerguntaResposta content
items.

Adding a new PerguntaResposta content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'PerguntaResposta' and click the 'Add' button to get to the add form.

    >>> browser.getControl('PerguntaResposta').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'PerguntaResposta' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'PerguntaResposta Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'PerguntaResposta' content item to the portal.

Updating an existing PerguntaResposta content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New PerguntaResposta Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New PerguntaResposta Sample' in browser.contents
    True

Removing a/an PerguntaResposta content item
--------------------------------

If we go to the home page, we can see a tab with the 'New PerguntaResposta
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New PerguntaResposta Sample' in browser.contents
    True

Now we are going to delete the 'New PerguntaResposta Sample' object. First we
go to the contents tab and select the 'New PerguntaResposta Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New PerguntaResposta Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New PerguntaResposta
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New PerguntaResposta Sample' in browser.contents
    False

Adding a new PerguntaResposta content item as contributor
------------------------------------------------

Not only site managers are allowed to add PerguntaResposta content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'PerguntaResposta' and click the 'Add' button to get to the add form.

    >>> browser.getControl('PerguntaResposta').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'PerguntaResposta' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'PerguntaResposta Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new PerguntaResposta content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Foto content type
===============================

In this section we are tesing the Foto content type by performing
basic operations like adding, updadating and deleting Foto content
items.

Adding a new Foto content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Foto' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Foto').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Foto' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Foto Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Foto' content item to the portal.

Updating an existing Foto content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Foto Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Foto Sample' in browser.contents
    True

Removing a/an Foto content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Foto
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Foto Sample' in browser.contents
    True

Now we are going to delete the 'New Foto Sample' object. First we
go to the contents tab and select the 'New Foto Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Foto Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Foto
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Foto Sample' in browser.contents
    False

Adding a new Foto content item as contributor
------------------------------------------------

Not only site managers are allowed to add Foto content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Foto' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Foto').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Foto' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Foto Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Foto content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Coluna content type
===============================

In this section we are tesing the Coluna content type by performing
basic operations like adding, updadating and deleting Coluna content
items.

Adding a new Coluna content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Coluna' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Coluna').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Coluna' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Coluna Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Coluna' content item to the portal.

Updating an existing Coluna content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Coluna Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Coluna Sample' in browser.contents
    True

Removing a/an Coluna content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Coluna
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Coluna Sample' in browser.contents
    True

Now we are going to delete the 'New Coluna Sample' object. First we
go to the contents tab and select the 'New Coluna Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Coluna Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Coluna
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Coluna Sample' in browser.contents
    False

Adding a new Coluna content item as contributor
------------------------------------------------

Not only site managers are allowed to add Coluna content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Coluna' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Coluna').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Coluna' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Coluna Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Coluna content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Album content type
===============================

In this section we are tesing the Album content type by performing
basic operations like adding, updadating and deleting Album content
items.

Adding a new Album content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Album' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Album').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Album' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Album Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Album' content item to the portal.

Updating an existing Album content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Album Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Album Sample' in browser.contents
    True

Removing a/an Album content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Album
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Album Sample' in browser.contents
    True

Now we are going to delete the 'New Album Sample' object. First we
go to the contents tab and select the 'New Album Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Album Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Album
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Album Sample' in browser.contents
    False

Adding a new Album content item as contributor
------------------------------------------------

Not only site managers are allowed to add Album content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Album' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Album').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Album' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Album Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Album content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)



