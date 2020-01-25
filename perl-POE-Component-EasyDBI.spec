#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	POE
%define	pnam	Component-EasyDBI
Summary:	POE::Component::EasyDBI - Perl extension for asynchronous non-blocking DBI calls in POE
#Summary(pl.UTF-8):	
Name:		perl-POE-Component-EasyDBI
Version:	1.23
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f1a61a2b5db177dd8355fcebc1aa299d
URL:		http://search.cpan.org/dist/POE-Component-EasyDBI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBI >= 1.38
BuildRequires:	perl-Error >= 0.15
BuildRequires:	perl-Params-Util
BuildRequires:	perl-POE >= 0.20
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module works by creating a new session, then spawning a child process
to do the DBI queries. That way, your main POE process can continue servicing
other clients.

The standard way to use this module is to do this:

    use POE;
    use POE::Component::EasyDBI;

    POE::Component::EasyDBI->spawn( ... );

    POE::Session->create( ... );

    POE::Kernel->run();



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Component/*.pm
%{perl_vendorlib}/POE/Component/EasyDBI
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
