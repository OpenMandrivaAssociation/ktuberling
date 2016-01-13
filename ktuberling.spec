Name:		ktuberling
Version:	15.12.1
Release:	1
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
%{_bindir}/ktuberling
%{_datadir}/applications/org.kde.ktuberling.desktop
%{_datadir}/ktuberling/pics/*.theme
%{_datadir}/ktuberling/pics/*.desktop
%{_datadir}/ktuberling/pics/*.svgz
%{_datadir}/ktuberling/pics/*.svg
%{_kde5_docdir}/*/*/ktuberling
%{_kde5_iconsdir}/hicolor/*/apps/ktuberling.png
%{_kde5_iconsdir}/hicolor/*/mimetypes/application-x-tuberling.png
%{_datadir}/ktuberling/sounds/en.soundtheme
%{_datadir}/ktuberling/sounds/en/*.ogg
%{_datadir}/kxmlgui5/ktuberling/ktuberlingui.rc


#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

