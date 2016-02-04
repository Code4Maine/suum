[![Stories in Ready](https://badge.waffle.io/Code4Maine/suum.png?label=ready&title=Ready)](https://waffle.io/Code4Maine/suum)
Suum
==============
[![Gitter](https://badges.gitter.im/Join Chat.svg)](https://gitter.im/code4maine/suum?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Suum is latin for property. This tool is a simple visualization of property
values as captured from CSV files of a city or counties property maps.

Start your engines, err projects!
---------------------------------

Your first order of business is to rename some things. Unless your project
is also called suum, you'll likely want to rename things. The easiest way
to get started is:

make name="<myproject_name>" rename

That should do all the important replacements. The final step will be removing
the .git folder and initializing your own repository and lastly tweaking the
setup.py file, else you're likely to give me credit for your project and to 
provide a pretty terribly confusing description to PyPI if your project ever
lands there.

Easy bootstrapping!
-------------------

Powered by the ubiquitous Makefile ... this should be pretty easy:

1. make install
2. make run
3. open your browser to: http://127.0.0.1:45000


Librarys, librarys, librarys!
-----------------------------

Of course, we could provide a vagrant file and a provisoner and all 
that jazz. But I'd rather provide a make file for installing everything
into a venv and let you muck about with libraries. Those of you on
Linux shouldn't have too much trouble installing the requisite development
libraries below. The names are for debian-based distros, but they 
exist for all major distros. 

On Mac it may be a little tricker. Homebrew will get you quite far, but
first you have to install the bloated XCode and the CLI tools.

The libraries are:

  * libmemcached-dev
  * libfreetype6-dev
  * libjpeg-dev

