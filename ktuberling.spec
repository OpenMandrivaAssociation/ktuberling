%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		ktuberling
Version:	19.07.90
Release:	1
Epoch:		1
Summary:	"Potato editor" game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/ktuberling/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake ninja cmake(ECM)
BuildRequires: 	cmake(KF5KDEGames)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Completion) cmake(KF5Config) cmake(KF5ConfigWidgets) cmake(KF5CoreAddons) cmake(KF5Crash) cmake(KF5DBusAddons) cmake(KF5I18n) cmake(KF5WidgetsAddons) cmake(KF5XmlGui) cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5PrintSupport) cmake(Qt5Svg) cmake(Qt5Widgets) cmake(Qt5Xml) cmake(Phonon4Qt5) cmake(Qt5Multimedia)

%description
KTuberling is a "potato editor" game intended for small children and adults
who remain young at heart. The game has no winner; the only purpose is to
make the funniest faces you can.

%files -f %{name}.lang
%{_bindir}/ktuberling
%{_datadir}/applications/org.kde.ktuberling.desktop
%{_datadir}/ktuberling/pics/*.theme
%{_datadir}/ktuberling/pics/*.desktop
%{_datadir}/ktuberling/pics/*.svgz
%{_datadir}/ktuberling/pics/*.svg
%{_kde5_iconsdir}/hicolor/*/apps/ktuberling.png
%{_kde5_iconsdir}/hicolor/*/mimetypes/application-x-tuberling.png
%{_datadir}/ktuberling/sounds/en.soundtheme
%{_datadir}/ktuberling/sounds/en/*.ogg
%{_datadir}/kxmlgui5/ktuberling/ktuberlingui.rc
%{_datadir}/metainfo/org.kde.ktuberling.appdata.xml
%lang(ca) %{_datadir}/ktuberling/sounds/ca.soundtheme
%lang(ca) %{_datadir}/ktuberling/sounds/ca
%lang(da) %{_datadir}/ktuberling/sounds/da.soundtheme
%lang(da) %{_datadir}/ktuberling/sounds/da
%lang(de) %{_datadir}/ktuberling/sounds/de.soundtheme
%lang(de) %{_datadir}/ktuberling/sounds/de
%lang(el) %{_datadir}/ktuberling/sounds/el.soundtheme
%lang(el) %{_datadir}/ktuberling/sounds/el
%lang(es) %{_datadir}/ktuberling/sounds/es.soundtheme
%lang(es) %{_datadir}/ktuberling/sounds/es
%lang(fi) %{_datadir}/ktuberling/sounds/fi.soundtheme
%lang(fi) %{_datadir}/ktuberling/sounds/fi
%lang(fr) %{_datadir}/ktuberling/sounds/fr.soundtheme
%lang(fr) %{_datadir}/ktuberling/sounds/fr
%lang(ga) %{_datadir}/ktuberling/sounds/ga.soundtheme
%lang(ga) %{_datadir}/ktuberling/sounds/ga
%lang(gl) %{_datadir}/ktuberling/sounds/gl.soundtheme
%lang(gl) %{_datadir}/ktuberling/sounds/gl
%lang(it) %{_datadir}/ktuberling/sounds/it.soundtheme
%lang(it) %{_datadir}/ktuberling/sounds/it
%lang(lt) %{_datadir}/ktuberling/sounds/lt.soundtheme
%lang(lt) %{_datadir}/ktuberling/sounds/lt
%lang(nds) %{_datadir}/ktuberling/sounds/nds.soundtheme
%lang(nds) %{_datadir}/ktuberling/sounds/nds
%lang(nl) %{_datadir}/ktuberling/sounds/nl.soundtheme
%lang(nl) %{_datadir}/ktuberling/sounds/nl
%lang(pt) %{_datadir}/ktuberling/sounds/pt.soundtheme
%lang(pt) %{_datadir}/ktuberling/sounds/pt
%lang(ro) %{_datadir}/ktuberling/sounds/ro.soundtheme
%lang(ro) %{_datadir}/ktuberling/sounds/ro
%lang(ru) %{_datadir}/ktuberling/sounds/ru.soundtheme
%lang(ru) %{_datadir}/ktuberling/sounds/ru
%lang(sl) %{_datadir}/ktuberling/sounds/sl.soundtheme
%lang(sl) %{_datadir}/ktuberling/sounds/sl
%lang(sr) %{_datadir}/ktuberling/sounds/sr.soundtheme
%lang(sr@ijekavian) %{_datadir}/ktuberling/sounds/sr@ijekavian.soundtheme
%lang(sr@ijekavianlatin) %{_datadir}/ktuberling/sounds/sr@ijekavianlatin.soundtheme
%lang(sr@latin) %{_datadir}/ktuberling/sounds/sr@latin.soundtheme
%lang(sr) %{_datadir}/ktuberling/sounds/sr
%lang(sv) %{_datadir}/ktuberling/sounds/sv.soundtheme
%lang(sv) %{_datadir}/ktuberling/sounds/sv
%lang(uk) %{_datadir}/ktuberling/sounds/uk.soundtheme
%lang(uk) %{_datadir}/ktuberling/sounds/uk
%lang(wa) %{_datadir}/ktuberling/sounds/wa.soundtheme
%lang(wa) %{_datadir}/ktuberling/sounds/wa

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
