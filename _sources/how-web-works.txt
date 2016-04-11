=============
How Web works
=============

The Internet is the backbone of the Web, the technical infrastructure
that makes the Web possible. At its most basic, the Internet is a large
network of computers which communicate all together.

History
=======

The history of the Internet is somewhat obscure. It began in the 1960s
as a US-army-funded research project, then evolved into a public infrastructure
in the 1980s with the support of many public universities and private companies.
The various technologies that support the Internet have evolved over time,
but the way it works hasn't changed that much: Internet is a way to connect
computers all together and ensure that, whatever happens, they find a way
to stay connected.

Simple network
==============

When two computers need to communicate, you have to link them,
either physically (usually with an Ethernet cable) or wirelessly
(for example with Wi-Fi or Bluetooth systems).
All modern computers can sustain any of those connections.

.. todo:: Insert picture

Such a network is not limited to two computers. You can connect as many
computers as you wish. But it gets complicated quickly. If you're trying
to connect, for example, ten computers, you need 45 cables, with nine plugs per
computer!

.. todo:: Insert picture

Network of networks
===================

.. todo:: TBD

Finding computers
=================

If you want to send a message to a computer, you have to specify which one.
Thus any computer linked to a network has a unique address to identify it,
called an "IP address" (where IP stands for `Internet Protocol`_).
It's an address made of a series of four numbers separated by dots,
for example: ``192.168.1.10``.

That's perfectly fine for computers, but we human beings have a hard time
remembering that sort of address. To make things easier, we can alias
an IP address with a human readable name called a domain name.
For example, ``google.com`` is the domain name used on top of the
IP address ``216.58.214.238``. So using the domain name is the easiest
way for us to reach a computer over the Internet.

Clients and servers
===================

Computers connected to the Web are called clients and servers.
A simplified diagram of how they interact might look like this:

.. todo:: Insert picture

* Clients are the typical Web user's Internet-connected devices
  (for example, your computer connected to your Wi-Fi, or your phone
  connected to your mobile network) and Web-accessing software available
  on those devices (usually a web browser like Firefox or Chrome).
* Servers are computers that store web-pages, sites, or apps.
  When a client device wants to access a web-page, a copy of the web-page
  is downloaded from the server onto the client machine to be displayed
  in the user's web browser.

The client and server we've described above don't tell the whole story.
There are many other parts involved, and we'll describe them below.

In addition to the client and the server, we also need to say hello to:

* **Your Internet connection:** Allows you to send and receive data on the Web.
  It's basically like the street between your house and the shop.
* **TCP/IP:** `Transmission Control Protocol`_ and Internet Protocol
  are communication protocols that define how data should travel
  across the Web. This is like the transport mechanisms that let you
  to place an order, go to the shop, and buy your goods.
  In our example, this is like a car or a bike (or your own two feet).
* **DNS:** `Domain Name System`_ Servers are like an address book for websites.
  When you type a web address in your browser, the browser looks at the DNS
  before retrieving the website. The browser needs to find out which server
  the website lives on, so it can send HTTP messages to the right place
  (see below). This is like looking up the address of the shop so you can
  access it.
* **HTTP:** `Hypertext Transfer Protocol`_ is an application protocol that
  defines a language for clients and servers to speak to each other.
  This is like the language you use to order your goods.
* **Component files:** A website is made up of many different files,
  which are like the different parts of the goods you buy from the shop.
  These files come in two main types:

  * **Code files:** Websites are built primarily from HTML, CSS, and
    JavaScript, though you'll meet other technologies a bit later.
  * **Assets:** This is a collective name for all the other stuff that makes up
    a website, such as images, music, video, Word documents, and PDFs.

So what happens, exactly?
=========================

When you type a web address into your browser:

#. The browser goes to the DNS server and finds the real address of the
   server that the website lives on.
#. The browser sends an HTTP request message to the server asking it to
   send a copy of the website to the client.
   This message, and all other data sent between the client and the server,
   is sent across your internet connection using TCP/IP.
#. Provided the server approves the client's request, the server sends
   the client a message like::

     HTTP/1.1 200 OK

#. The browser assembles the small chunks into a complete website and
   displays it to you.

DNS explained
=============

Real web addresses aren't the nice, memorable strings you type into your
address bar to find your favorite websites. They are strings of numbers,
like this: ``216.58.214.238``.

This is called an IP address, and it represents a unique location on the Web.
However, it's not very easy to remember, is it?
That's why Domain Name Servers were invented.
These are special servers that match up a web address you type into y
our browser (like ``google.com``) to the web-site's real (IP) address.

Websites can be reached directly via their IP addresses.
Try going to the Google website by typing ``216.58.214.238``
into the address bar on a new browser tab.

.. note::

    Based on articles by Mozilla Contributors
    licensed under `CC-BY-SA 2.5 <http://creativecommons.org/licenses/by-sa/2.5/>`_:

    * `How does the Internet work? <https://developer.mozilla.org/en-US/Learn/Common_questions/How_does_the_Internet_work>`__
    * `How the Web works <https://developer.mozilla.org/en-US/Learn/Getting_started_with_the_web/How_the_Web_works>`__

.. _Internet Protocol: https://en.wikipedia.org/wiki/Internet_Protocol
.. _Transmission Control Protocol: https://en.wikipedia.org/wiki/Transmission_Control_Protocol
.. _Domain Name System: https://en.wikipedia.org/wiki/Domain_Name_System
.. _Hypertext Transfer Protocol: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol