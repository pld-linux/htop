Summary:	An interactive process viewer
Summary(hu.UTF-8):	Egy interaktív processz megjelenítő
Summary(pl.UTF-8):	Interaktywna przeglądarka procesów
Name:		htop
Version:	0.9
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/htop/%{name}-%{version}.tar.gz
# Source0-md5:	7c5507f35f363f3f40183a2ba3c561f8
Patch0:		%{name}-desktop.patch
Patch2:		%{name}-field-titles.patch
URL:		http://htop.sourceforge.net/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gcc >= 5:3.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	python
BuildRequires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
htop is an interactive text-mode process viewer for Linux. It aims to
be a better 'top'.

%description -l hu.UTF-8
htop egy interaktív szöveges módú processz megjelenítő Linuxra.
Lényegében egy jobb 'top' szeretne lenni.

%description -l pl.UTF-8
htop jest interaktywną, tekstową przeglądarką procesów dla Linuksa.
Jej celem jest bycie lepszą odmianą programu 'top'.

%prep
%setup -q
%patch0 -p1
%patch2 -p1

# don't require /proc at build time
sed '/^AC_CHECK_FILE($PROCDIR/d' -i configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncursesw"
LDFLAGS="%{rpmldflags} -ltinfow"
%configure \
	--enable-openvz \
	--enable-unicode \
	--enable-vserver
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/htop
%{_desktopdir}/htop.desktop
%{_pixmapsdir}/htop.png
%{_mandir}/man1/htop.1*
