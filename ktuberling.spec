Name:		ktuberling
Version:	4.10.0
Release:	1
Epoch:		1
Summary:	KTuberling: "potato editor" game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ktuberling/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
KTuberling is a "potato editor" game intended for small children and adults
who remain young at heart. The game has no winner; the only purpose is to
make the funniest faces you can.

%files
%{_kde_bindir}/ktuberling
%{_kde_applicationsdir}/ktuberling.desktop
%{_kde_appsdir}/ktuberling
%{_kde_docdir}/*/*/ktuberling
%{_kde_iconsdir}/hicolor/*/apps/ktuberling.png
%{_kde_iconsdir}/hicolor/*/mimetypes/application-x-tuberling.png

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

