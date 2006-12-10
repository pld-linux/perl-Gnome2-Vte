#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gnome2
%define		pnam	Vte
Summary:	Perl vte bindings
Summary(pl):	Wi±zania vte dla Perla
Name:		perl-Gnome2-Vte
Version:	0.08
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c547adf2ed15ce223350094507b4b8a7
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	vte-devel >= 0.13.7
BuildRequires:	perl-ExtUtils-Depends >= 0.205
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.07
BuildRequires:	perl-Glib >= 1.132
BuildRequires:	perl-Gtk2 >= 1.133
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Glib >= 1.132
Requires:	perl-Gtk2 >= 1.133
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl access to vte library.

%description -l pl
Ten modu³ daje dostêp z poziomu Perla do biblioteki vte.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gnome2/Vte/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/Gnome2/Vte.pm
%dir %{perl_vendorarch}/Gnome2/Vte
%{perl_vendorarch}/Gnome2/Vte/Install
%dir %{perl_vendorarch}/auto/Gnome2/Vte
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome2/Vte/*.so
%{perl_vendorarch}/auto/Gnome2/Vte/*.bs
%{_mandir}/man3/*
