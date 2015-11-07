Name:          gimp-saveforweb-plugin
Version:       0.29.3
Release:       3%{?dist}
Summary:       Save for web plug-in for GIMP

License:       GPLv2+
URL:           http://registry.gimp.org/node/33
Source0:       http://registry.gimp.org/files/gimp-save-for-web-%{version}.tar.bz2
Patch0:        %{name}-fsf.patch

BuildRequires: gimp-devel >= 2.4.0
BuildRequires: intltool
Requires:      gimp >= 2.4

%description
Save for Web allows to find compromise between minimal file size
and acceptable quality of image quickly. While adjusting various
settings, you may explore how image quality and file size change.
Options to reduce file size of an image include setting compression
quality, number or colors, resizing, cropping, Exif information
removal, etc.

%prep
%setup -q -n gimp-save-for-web-%{version}
%patch0 -p1

%build
%configure
%make_build

%install
%make_install
%find_lang gimp20-save-for-web

%files -f gimp20-save-for-web.lang
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_libdir}/gimp/2.0/plug-ins/webexport
%{_datadir}/gimp-save-for-web

%changelog
* Sat Nov 07 2015 Maxim Orlov <murmansksity@gmail.com> - 0.29.3-3.R
- Removed unnecessary BR

* Sat Jul 25 2015 Maxim Orlov <murmansksity@gmail.com> - 0.29.3-2.R
- Fixed incorrect-fsf-address lint error.

* Mon Jul 20 2015 Maxim Orlov <murmansksity@gmail.com> - 0.29.3-1.R
- Initial package.
