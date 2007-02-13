Summary:	Kalamaris - mathematical application for KDE
Summary(pl.UTF-8):	Program matematyczny dla KDE
Name:		kalamaris
Version:	0.7.1
Release:	3
License:	GPL
Group:		Applications/Math
Source0:	http://devel-home.kde.org/~larrosa/bin/%{name}-%{version}.tar.bz2
# Source0-md5:	814c8c592dbf0ffe76b36ba157d8b2b4
Patch0:		%{name}-desktop.patch
URL:		http://devel-home.kde.org/~larrosa/kalamaris.html
BuildRequires:	automake
BuildRequires:	gmp-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Kalamaris is the next generation scientific applications. While
similar to Mathematica in some aspects, it offers a new approach to
solve mathematical problems in an easy and intuitive way.

%description -l pl.UTF-8
Kalamaris należy do nowej generacji naukowych aplikacji. Podczas gdy
jest podobny do Mathematica pod pewnymi względami - oferuje nowe
możliwości rozwiązywania problemów matematycznych w łatwy i intuicyjny
sposób.

%package examples
Summary:	Kalamaris - examples
Summary(pl.UTF-8):	Kalamaris - przyklady
Group:		Applications/Math

%description examples
Kalamaris is the next generation scientific applications. While
similar to Mathematica in some aspects, it offers a new approach to
solve mathematical problems in an easy and intuitive way.

%description examples -l pl.UTF-8
Kalamaris należy do nowej generacji naukowych aplikacji. Podczas gdy
jest podobny do Mathematica pod pewnymi względami - oferuje nowe
możliwości rozwiązywania problemów matematycznych w łatwy i intuicyjny
sposób.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
cp -f /usr/share/automake/config.* admin
%configure \
	KDEDIR=%{_libdir} \
	--with-qt-includes=%{_includedir}/qt \
	--with-qt-libraries=%{_libdir} \
	--x-includes=%{_includedir}/kde \
	--with-extra-includes=%{_includedir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	applnkdir=%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/kalamaris
%{_datadir}/apps/kalamaris
%{_desktopdir}/*.desktop

%files examples
%defattr(644,root,root,755)
%doc kalamaris/examples/*
