Summary:	Shared functions for Ayatana Indicator Display Objects (GTK+ 3.x version)
Summary(pl.UTF-8):	Funkcje współdzielone dla obiektów wyświetlania wskaźników Ayatana (wersja dla GTK+ 3.x)
Name:		ido-gtk3
Version:	12.10.2
Release:	2
License:	LGPL v2.1 or LGPL v3
Group:		Libraries
#Source0Download: https://launchpad.net/ido/+download
Source0:	https://launchpad.net/ido/12.10/%{version}/+download/ido-%{version}.tar.gz
# Source0-md5:	9910f4e9a3bf07a88dff08b32d048a8f
URL:		https://launchpad.net/ido
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	which
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shared functions for Ayatana Indicator Display Objects (GTK+ 3.x
version).

%description -l pl.UTF-8
Funkcje współdzielone dla obiektów wyświetlania wskaźników Ayatana
(wersja dla GTK+ 3.x).

%package devel
Summary:	Development files for ido library (GTK+ 3.x version)
Summary(pl.UTF-8):	Pliki programistyczne biblioteki ido (wersja dla GTK+ 3.x)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.32.0
Requires:	gtk+3-devel >= 3.4.0

%description devel
This package contains the header files for developing applications
that use ido library (GTK+ 3.x version).

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę ido (w wersji dla GTK+ 3.x).

%prep
%setup -q -n ido-%{version}

# gtk+ deprecations
%{__sed} -i -e 's|-Werror||g' src/Makefile.am

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_libdir}/libido3-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libido3-0.1.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libido3-0.1.so
%{_includedir}/libido3-0.1
%{_pkgconfigdir}/libido3-0.1.pc
