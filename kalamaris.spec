%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

Summary:	Kalamaris - mathematical application for KDE
Summary(pl):	Program matematyczny dla KDE
Name:		kalamaris
Version:	0.6.0
Release:	1
Group:		Applications/Math
Group(pl):	Aplikacje/Matematyczne
Copyright:	GPL
Source0:	http://www.arrakis.es/~rlarrosa/bin/%{name}-%{version}.tar.bz2
Patch0:		%{name}-unlink.patch
Patch1:		%{name}-make.patch
BuildRequires:	qt >= 2.2.0
BuildRequires:  kdelibs >= 2.0
URL:		http://www.arrakis.es/~rlarrosa/kalamaris.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kalamaris is the next generation scientific applications. While similar to
Mathematica in some aspects, it offers a new approach to solve mathematical
problems in an easy and intuitive way.

%description -l pl
Kalamaris nale¿y do nowej generacji naukowych aplikacji. Podczas gdy jest
podobny do Mathematica pod pewnymi wzglêdami - oferuje nowe mo¿liwo¶ci
rozwi±zywania problemów matematycznych w ³atwy i intuicyjny sposób.

%package examples
Summary:	Kalamaris - examples
Summary(pl):	Kalamaris - przyklady
Group:		Applications/Math
Group(pl):	Aplikacje/Matematyczne

%description examples
Kalamaris is the next generation scientific applications. While similar to
Mathematica in some aspects, it offers a new approach to solve mathematical
problems in an easy and intuitive way.

%description examples -l pl
Kalamaris nale¿y do nowej generacji naukowych aplikacji. Podczas gdy jest
podobny do Mathematica pod pewnymi wzglêdami - oferuje nowe mo¿liwo¶ci
rozwi±zywania problemów matematycznych w ³atwy i intuicyjny sposób.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
    --with-qt-includes=/usr/X11R6/include/qt \
    --with-qt-libraries=/usr/X11R6/lib \
    --x-includes=/usr/X11R6/include/kde \
    --with-extra-includes=/usr/X11R6/include
    
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_applnkdir}/Applications/kalamaris.desktop
%{_datadir}/apps/kalamaris/*
%attr(755,root,root) %{_bindir}/kalamaris
%doc README
%doc COPYING

%files examples
%doc kalamaris/examples/*
