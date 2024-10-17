%define upstream_name    Devel-FindRef
%define upstream_version 1.422

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	6

Summary:    Where is that reference to my variable hiding?
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(common::sense)
BuildRequires: perl-devel

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
Tracking down reference problems (e.g. you expect some object to be
destroyed, but there are still references to it that keep it alive) can be
very hard. Fortunately, perl keeps track of all its values, so tracking
references "backwards" is usually possible.

The 'track' function can help track down some of those references back to
the variables containing them.

For example, for this fragment:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.422.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.422.0-3
+ Revision: 681399
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.422.0-2mdv2011.0
+ Revision: 555233
- rebuild
- update to 1.422

* Mon Aug 31 2009 Jérôme Quelin <jquelin@mandriva.org> 1.422.0-1mdv2010.0
+ Revision: 422825
- adding missing buildrequires:
- update to 1.422

* Sat Aug 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.421.0-1mdv2010.0
+ Revision: 422081
- update to 1.421

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.420.0-1mdv2010.0
+ Revision: 395133
- update to 1.42

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 1.410.0-1mdv2010.0
+ Revision: 390468
- import perl-Devel-FindRef


* Mon Jun 29 2009 cpan2dist 1.41-1mdv
- initial mdv release, generated with cpan2dist

