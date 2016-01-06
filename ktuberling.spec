Name:		ktuberling
Version:	15.12.0
Release:	2
Epoch:		1
Summary:	"Potato editor" game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ktuberling/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	kdelibs4-devel
BuildRequires: 	cmake(KDEGames)
BuildRequires:	cmake(Qt5Test)

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
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build


