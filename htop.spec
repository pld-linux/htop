Summary:	An interactive process viewer
Summary(pl):	Interaktywna przegl�darka proces�w
Name:		htop
Version:	0.6
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/htop/%{name}-%{version}.tar.gz
# Source0-md5:	c00b1dba101569a055ed260e06a25596
URL:		http://htop.sourceforge.net/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
htop is an interactive text-mode process viewer for Linux. It aims to
be a better 'top'.

%description -l pl
htop jest interaktywn�, tekstow� przegl�dark� proces�w dla Linuksa. Jej
celem jest bycie lepsz� odmian� 'topu'.

%prep
%setup -q

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
