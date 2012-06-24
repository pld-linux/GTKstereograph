Summary:	GTKstereograph, an advanced stereogram generator
Summary(pl):	GTKstereograph, zaawansowany generator stereogram�w
Name:		GTKstereograph
Version:	0.17a
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	http://download.sourceforge.net/stereograph/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_lt.patch
URL:		http://stereograph.sourceforge.net/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libpng >= 1.0.8
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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

%description -l pl
GTKstereograph jest graficznym interfejsem u�ytkownika do aktualnego
generatora stereogram�w. Stereograph jest generatorem stereogram�w.
Dok�adniej jest to generator pojedynczych obraz�w stereogramowych (SIS).
Program ten produkuje dwuwymiarowe obrazy, kt�re wydaj� si� by�
tr�jwymiarowe (surely you know the famous works of "The Magic Eye",
Stereograph produces the same output). NIE potrzebujesz wcale pary
r�nokolorowych okular�w, aby to zobaczy� - (prawie) ka�dy mo�e si�
tego nauczy�.

Autorzy:
- -------- Fabian Januszewski <fabian.linux@januszewski.de>

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
automake -a -c
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/GTKstereograph
