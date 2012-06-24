Summary:	Kalamaris - mathematical application for KDE
Summary(pl):	Program matematyczny dla KDE
Name:		kalamaris
Version:	0.6.0
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://perso.wanadoo.es/antlarr/bin/%{name}-%{version}.tar.bz2
# Source0-md5:	1e7204c1ae37669fccc575e72684ba96
Patch0:		%{name}-unlink.patch
Patch1:		%{name}-make.patch
URL:		http://perso.wanadoo.es/antlarr/kalamaris.html
BuildRequires:	kdelibs-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Kalamaris is the next generation scientific applications. While
similar to Mathematica in some aspects, it offers a new approach to
solve mathematical problems in an easy and intuitive way.

%description -l pl
Kalamaris nale�y do nowej generacji naukowych aplikacji. Podczas gdy
jest podobny do Mathematica pod pewnymi wzgl�dami - oferuje nowe
mo�liwo�ci rozwi�zywania problem�w matematycznych w �atwy i intuicyjny
spos�b.

%package examples
Summary:	Kalamaris - examples
Summary(pl):	Kalamaris - przyklady
Group:		Applications/Math

%description examples
Kalamaris is the next generation scientific applications. While
similar to Mathematica in some aspects, it offers a new approach to
solve mathematical problems in an easy and intuitive way.

%description examples -l pl
Kalamaris nale�y do nowej generacji naukowych aplikacji. Podczas gdy
jest podobny do Mathematica pod pewnymi wzgl�dami - oferuje nowe
mo�liwo�ci rozwi�zywania problem�w matematycznych w �atwy i intuicyjny
spos�b.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure2_13 \
	--with-qt-includes=%{_includedir}/qt \
	--with-qt-libraries=%{_libdir} \
	--x-includes=%{_includedir}/kde \
	--with-extra-includes=%{_includedir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Mathematics

mv -f $RPM_BUILD_ROOT%{_applnkdir}/Applications/kalamaris.desktop $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Mathematics/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/kalamaris
%{_applnkdir}/Scientific/Mathematics/*
%{_datadir}/apps/kalamaris

%files examples
%defattr(644,root,root,755)
%doc kalamaris/examples/*
