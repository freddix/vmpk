Summary:	Virtual MIDI piano keyboard
Name:		vmpk
Version:	0.5.0
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/vmpk/%{name}-%{version}.tar.bz2
# Source0-md5:	2f0d31454a6dd1ad12ac9d8db1358200
BuildRequires:	QtGui-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake
BuildRequires:	libxslt-progs
BuildRequires:	pkg-config
BuildRequires:	qt-linguist
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virtual MIDI Piano Keyboard is a MIDI event generator and receiver.
It doesn't produce any sound by itself, but can be used to drive a MIDI
synthesizer (either hardware or software, internal or external).

%prep
%setup -q

sed -i -e 's|Categories=.*|Categories=Qt;AudioVideo;Audio;Midi;|' %{name}.desktop

%build
mkdir build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/vmpk
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/vmpk.*
%{_mandir}/man1/vmpk.1*

