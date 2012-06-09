# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       plymouth-lite
Summary:    Boot splash screen based on Fedora's Plymouth code
Version:    0.6.0
Release:    1
Group:      System/Base
License:    GPLv2
URL:        http://www.moblin.org
Source0:    %{name}-0.6.0.tar.bz2
Source1:    %{name}-start.service
Source2:    %{name}-halt.service
Source3:    %{name}-reboot.service
Source4:    %{name}-poweroff.service
Source100:  plymouth-lite.yaml
Patch0:     cursor.patch
Patch1:     plymouth-resize.patch
Patch2:     plymouth-fix-build.patch
Patch3:     plymouth-lite-0.6.0-dont_install_splash.patch
Patch4:     plymouth-fix-cflags.patch
Patch5:     plymouth-lite-0.6.0-png-set-gray.patch
Requires:   openshellfish-backgrounds
Requires:   systemd
Requires(preun): systemd
Requires(post): systemd
Requires(postun): systemd
BuildRequires:  pkgconfig(libpng)
Provides:   plymouth-lite-osf


%description
Boot splash screen based on Fedora's Plymouth code.




%prep
%setup -q -n %{name}-%{version}

# cursor.patch
%patch0 -p1
# plymouth-resize.patch
%patch1 -p1
# plymouth-fix-build.patch
%patch2 -p1
# plymouth-lite-0.6.0-dont_install_splash.patch
%patch3 -p1
# plymouth-fix-cflags.patch
%patch4 -p1
# plymouth-lite-0.6.0-png-set-gray.patch
%patch5 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
install -D -m 644 %{SOURCE1} %{buildroot}/lib/systemd/system/%{name}-start.service
install -d %{buildroot}/lib/systemd/system/sysinit.target.wants/
ln -s ../%{name}-start.service %{buildroot}/lib/systemd/system/sysinit.target.wants/%{name}-start.service

install -D -m 644 %{SOURCE2} %{buildroot}/lib/systemd/system/%{name}-halt.service
install -d %{buildroot}/lib/systemd/system/halt.target.wants/
ln -s ../%{name}-halt.service %{buildroot}/lib/systemd/system/halt.target.wants/%{name}-halt.service

install -D -m 644 %{SOURCE3} %{buildroot}/lib/systemd/system/%{name}-reboot.service
install -d %{buildroot}/lib/systemd/system/reboot.target.wants/
ln -s ../%{name}-reboot.service %{buildroot}/lib/systemd/system/reboot.target.wants/%{name}-reboot.service

install -D -m 644 %{SOURCE4} %{buildroot}/lib/systemd/system/%{name}-poweroff.service
install -d %{buildroot}/lib/systemd/system/poweroff.target.wants/
ln -s ../%{name}-poweroff.service %{buildroot}/lib/systemd/system/poweroff.target.wants/%{name}-poweroff.service
# << install post


%preun
systemctl stop %{name}-start.service
systemctl stop %{name}-halt.service
systemctl stop %{name}-reboot.service
systemctl stop %{name}-poweroff.service

%post
systemctl daemon-reload
systemctl reload-or-try-restart %{name}-start.service
systemctl reload-or-try-restart %{name}-halt.service
systemctl reload-or-try-restart %{name}-reboot.service
systemctl reload-or-try-restart %{name}-poweroff.service

%postun
systemctl daemon-reload


%files
%defattr(-,root,root,-)
# >> files
%{_bindir}/ply-image
/lib/systemd/system/%{name}-start.service
/lib/systemd/system/sysinit.target.wants/%{name}-start.service
/lib/systemd/system/%{name}-halt.service
/lib/systemd/system/halt.target.wants/%{name}-halt.service
/lib/systemd/system/%{name}-reboot.service
/lib/systemd/system/reboot.target.wants/%{name}-reboot.service
/lib/systemd/system/%{name}-poweroff.service
/lib/systemd/system/poweroff.target.wants/%{name}-poweroff.service
# << files


