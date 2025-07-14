Summary:	Box package manager program and library
Summary(pl.UTF-8):	Program i biblioteka zarządcy pakietów Box
Name:		box
Version:	0.1.13
Release:	1
License:	GPL v2
Group:		Applications/Archiving
Source0:	http://download.gna.org/pingwinek/releases/box/%{name}-%{version}.tar.bz2
# Source0-md5:	b382a5bf67340c7e5cc851c1f99fbe6e
Patch0:		%{name}-build.patch
Patch1:		%{name}-flags.patch
URL:		http://home.gna.org/pingwinek/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3
Requires:	glib2 >= 1:2.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Box package manager program and library, designed for Pingwinek
distribution.

%description -l pl.UTF-8
Program i biblioteka zarządcy pakietów Box, zaprojektowane dla
dystrybucji Pingwinek.

%package devel
Summary:	Header files for Box library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Box
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.14.0

%description devel
Header files for Box library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Box.

%package static
Summary:	Static Box library
Summary(pl.UTF-8):	Statyczna biblioteka Box
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Box library.

%description static -l pl.UTF-8
Statyczna biblioteka Box.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libbox.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/box
%attr(755,root,root) %{_bindir}/box-info
%attr(755,root,root) %{_bindir}/box-vercmp
%attr(755,root,root) %{_bindir}/box-db-manager
%attr(755,root,root) %{_bindir}/box-query
%attr(755,root,root) %{_bindir}/box-repos
%attr(755,root,root) %{_bindir}/box-not-found
%attr(755,root,root) %{_libdir}/libbox.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbox.so.0
%dir %{_libdir}/box
%{_libdir}/box/macros
%dir %{_sysconfdir}/box
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/box/box-repos.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbox.so
%{_includedir}/libbox
%{_pkgconfigdir}/libbox.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libbox.a
