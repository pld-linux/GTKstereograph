Summary: GTKstereograph, an advanced stereogram generator
Name: GTKstereograph
%define version 0.11a
Version: %{version}
Release: 1
Group: Applications/Graphics
Copyright: GPL
Source: GTKstereograph-%{version}.tar.gz
URL: http://home2.ecore.net/januszewski/linux/stereograph.html

%description
GTKstereograph is a graphical user interface for the current stereograph
renderer.
Stereograph is a stereogram generator. In detail it is a single image
stereogram (SIS) generator. That's a program that produces twodimensional
images that seem to be threedimensional (surely you know the famous works of
"The Magic Eye", Stereograph produces the same output). You do _not_ need
any pair of colored spectacles to regard them - everyone can learn it.   

Authors:
--------
    Fabian Januszewski <fabian.linux@januszewski.de>

%prep
%setup

%build
./configure
make

%install
make install

%files
/usr/local/bin/GTKstereograph

%doc AUTHORS COPYING ChangeLog NEWS README
