%define upstream_name    Devel-FindRef
%define upstream_version 1.421

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Where is that reference to my variable hiding?
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz


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


