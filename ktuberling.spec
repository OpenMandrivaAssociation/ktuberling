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
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5KDELibs4Support)

%description
KTuberling is a "potato editor" game intended for small children and adults
who remain young at heart. The game has no winner; the only purpose is to
make the funniest faces you can.

%files
%{_kde5_bindir}/ktuberling
%{_kde5_applicationsdir}/ktuberling.desktop
%{_kde5_appsdir}/ktuberling
%{_kde5_docdir}/*/*/ktuberling
%{_kde5_iconsdir}/hicolor/*/apps/ktuberling.png
%{_kde5_iconsdir}/hicolor/*/mimetypes/application-x-tuberling.png
%{_kde5_prefix}//ktuberling/pics/*.*
%{_kde5_prefix}//ktuberling/sounds/en/*.ogg

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install


