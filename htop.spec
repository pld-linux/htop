Summary:	An interactive process viewer
Summary(pl):	Interaktywna przegl±darka procesów
Name:		htop
Version:	0.5.2
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/htop/%{name}-%{version}.tar.gz
# Source0-md5:	e1a3f03971a3868315c4c1f92aee9b7f
Patch0:		%{name}-home_etc.patch
URL:		http://htop.sourceforge.net/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
htop is an interactive text-mode process viewer for Linux. It aims to
be a better 'top'.

%description -l pl
htop jest interaktywn±, tekstow± przegl±dark± procesów dla Linuksa. Jej
celem jest bycie lepsz± odmian± 'topu'.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
