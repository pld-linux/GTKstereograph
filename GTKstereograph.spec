Summary:	GTKstereograph, an advanced stereogram generator
Summary(pl.UTF-8):	GTKstereograph, zaawansowany generator stereogramów
Name:		GTKstereograph
Version:	0.18b
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Vendor:		Fabian Januszewski <fabian.linux@januszewski.de>
Source0:	http://dl.sourceforge.net/stereograph/%{name}-%{version}.tar.gz
# Source0-md5:	e908e51f16a510275fca656047031130
Patch0:		%{name}-make.patch
URL:		http://stereograph.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTKstereograph is a graphical user interface for the current
stereograph renderer. Stereograph is a stereogram generator. In detail
it is a single image stereogram (SIS) generator. That's a program that
produces twodimensional images that seem to be threedimensional
(surely you know the famous works of "The Magic Eye", Stereograph
produces the same output). You do _not_ need any pair of colored
spectacles to regard them - everyone can learn it.

%description -l pl.UTF-8
GTKstereograph jest graficznym interfejsem użytkownika do aktualnego
generatora stereogramów. Stereograph jest generatorem stereogramów.
Dokładniej jest to generator pojedynczych obrazów stereogramowych
(SIS). Program ten produkuje dwuwymiarowe obrazy, które wydają się być
trójwymiarowe (surely you know the famous works of "The Magic Eye",
Stereograph produces the same output). NIE potrzebujesz wcale pary
różnokolorowych okularów, aby to zobaczyć - (prawie) każdy może się
tego nauczyć.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure

%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	LXLIBS="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/stereograph
%attr(755,root,root) %{_bindir}/GTKstereograph
%{_datadir}/stereograph
%{_mandir}/man1/stereograph.1*
