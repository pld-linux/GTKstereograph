Summary:	GTKstereograph, an advanced stereogram generator
Summary(pl):	GTKstereograph, zaawansowany generator stereogram�w
Name:		GTKstereograph
Version:	0.17a
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Vendor:		Fabian Januszewski <fabian.linux@januszewski.de>
Source0:	http://dl.sourceforge.net/stereograph/%{name}-%{version}.tar.gz
# Source0-md5:	35c1c42cbee4ba0d7d0d721ea5d3d8ec
Patch0:		%{name}-am_lt.patch
URL:		http://stereograph.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtool
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

%description -l pl
GTKstereograph jest graficznym interfejsem u�ytkownika do aktualnego
generatora stereogram�w. Stereograph jest generatorem stereogram�w.
Dok�adniej jest to generator pojedynczych obraz�w stereogramowych (SIS).
Program ten produkuje dwuwymiarowe obrazy, kt�re wydaj� si� by�
tr�jwymiarowe (surely you know the famous works of "The Magic Eye",
Stereograph produces the same output). NIE potrzebujesz wcale pary
r�nokolorowych okular�w, aby to zobaczy� - (prawie) ka�dy mo�e si�
tego nauczy�.

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
