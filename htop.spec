Summary:	An interactive process viewer
Summary(hu.UTF-8):	Egy interaktív processz megjelenítő
Summary(pl.UTF-8):	Interaktywna przeglądarka procesów
Name:		htop
Version:	3.4.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://github.com/htop-dev/htop/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	bd4e4bded1a286a3905a305d702b79ea
URL:		https://htop.dev/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	gcc >= 5:3.0
BuildRequires:	libcap-devel >= 2.21
BuildRequires:	libnl-devel >= 3.0
BuildRequires:	libunwind-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libcap-libs >= 2.21
Requires:	libnl >= 3.0
Suggests:	lm_sensors-libs
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

# don't require /proc at build time
sed 's@^[[:space:]]*AC_CHECK_FILE($PROCDIR.*@:@' -i configure.ac

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%{_iconsdir}/hicolor/scalable/apps/htop.svg
%{_pixmapsdir}/htop.png
%{_mandir}/man1/htop.1*
