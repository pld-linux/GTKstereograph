Summary:	GTKstereograph, an advanced stereogram generator
Summary(pl):	GTKstereograph, zaawansowany generator stereogramów
Name:		GTKstereograph
Version:	0.17a
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://download.sourceforge.net/stereograph/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_lt.patch
URL:		http://stereograph.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtool
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

%description -l pl
GTKstereograph jest graficznym interfejsem u¿ytkownika do aktualnego
generatora stereogramów. Stereograph jest generatorem stereogramów.
Dok³adniej jest to generator pojedynczych obrazów stereogramowych (SIS).
Program ten produkuje dwuwymiarowe obrazy, które wydaj± siê byæ
trójwymiarowe (surely you know the famous works of "The Magic Eye",
Stereograph produces the same output). NIE potrzebujesz wcale pary
ró¿nokolorowych okularów, aby to zobaczyæ - (prawie) ka¿dy mo¿e siê
tego nauczyæ.

Autorzy:
- -------- Fabian Januszewski <fabian.linux@januszewski.de>

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/GTKstereograph
