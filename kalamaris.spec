Summary:	Kalamaris - mathematical application for KDE
Summary(pl):	Program matematyczny dla KDE
Name:		kalamaris
Version:	0.7.1
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://devel-home.kde.org/~larrosa/bin/%{name}-%{version}.tar.bz2
# Source0-md5:	814c8c592dbf0ffe76b36ba157d8b2b4
URL:		http://devel-home.kde.org/~larrosa/kalamaris.html
BuildRequires:	gmp-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

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
%setup -q -n %{name}

%build
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure \
	--with-qt-includes=%{_includedir}/qt \
	--with-qt-libraries=%{_libdir} \
	--x-includes=%{_includedir}/kde \
	--with-extra-includes=%{_includedir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Mathematics
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Office/kalamaris.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Scientific/Mathematics

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/kalamaris
%{_applnkdir}/Scientific/Mathematics/*.desktop
%{_datadir}/apps/kalamaris

%files examples
%defattr(644,root,root,755)
%doc kalamaris/examples/*
