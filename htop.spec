Summary:	An interactive process viewer
Summary(pl.UTF-8):	Interaktywna przeglądarka procesów
Name:		htop
Version:	0.7
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/htop/%{name}-%{version}.tar.gz
# Source0-md5:	4afc961fa709167e1b434682897991f9
Patch0:		%{name}-desktop.patch
URL:		http://htop.sourceforge.net/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gcc >= 5:3.0
BuildRequires:	ncurses-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
htop is an interactive text-mode process viewer for Linux. It aims to
be a better 'top'.

%description -l pl.UTF-8
htop jest interaktywną, tekstową przeglądarką procesów dla Linuksa.
Jej celem jest bycie lepszą odmianą programu 'top'.

%prep
%setup -q
%patch0 -p1
%{__sed} -i -e 's/curses.h/ncurses\/curses.h/' configure.ac

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="$CPPFLAGS -I/usr/include/ncurses"
%configure \
	--enable-openvz
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
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/htop.desktop
%{_mandir}/man1/*
%{_pixmapsdir}/htop.png
