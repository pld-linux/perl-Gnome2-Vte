#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires DISPLAY)
#
%define		pdir	Gnome2
%define		pnam	Vte
Summary:	Perl vte bindings
Summary(pl.UTF-8):	Wiązania vte dla Perla
Name:		perl-Gnome2-Vte
Version:	0.11
Release:	7
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://downloads.sourceforge.net/gtk2-perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1cb5cdfcd41873e55e923e72e64d922c
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	perl-ExtUtils-Depends >= 0.205
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.07
BuildRequires:	perl-Glib-devel >= 1.132
BuildRequires:	perl-Gtk2-devel >= 1.133
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	vte0-devel >= 0.13.7
Requires:	perl-Glib >= 1.132
Requires:	perl-Gtk2 >= 1.133
Requires:	vte0 >= 0.13.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl access to vte library.

%description -l pl.UTF-8
Ten moduł daje dostęp z poziomu Perla do biblioteki vte.

%package devel
Summary:	Development files for Perl Gnome2-Vte bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Gnome2-Vte dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	perl-Glib-devel >= 1.132
Requires:	perl-Gtk2-devel >= 1.133
Requires:	vte0-devel >= 0.13.7

%description devel
Development files for Perl Gnome2-Vte bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Gnome2-Vte dla Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/Vte/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%{perl_vendorarch}/Gnome2/Vte.pm
%dir %{perl_vendorarch}/Gnome2/Vte
%dir %{perl_vendorarch}/auto/Gnome2/Vte
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Vte/Vte.so
%{_mandir}/man3/Gnome2::Vte*.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Gnome2/Vte/Install
