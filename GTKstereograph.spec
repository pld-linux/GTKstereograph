Summary:	GTKstereograph, an advanced stereogram generator
Name:		GTKstereograph
Version:	0.11a
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	http://home2.ecore.net/januszewski/linux/stereograph/%{name}-%{version}.tar.gz
URL:		http://home2.ecore.net/januszewski/linux/stereograph.html
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GTKstereograph is a graphical user interface for the current
stereograph renderer. Stereograph is a stereogram generator. In detail
it is a single image stereogram (SIS) generator. That's a program that
produces twodimensional images that seem to be threedimensional
(surely you know the famous works of "The Magic Eye", Stereograph
produces the same output). You do _not_ need any pair of colored
spectacles to regard them - everyone can learn it.

Authors:
- -------- Fabian Januszewski <fabian.linux@januszewski.de>

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/GTKstereograph
