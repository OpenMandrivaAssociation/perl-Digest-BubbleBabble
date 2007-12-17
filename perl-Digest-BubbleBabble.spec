%define module	Digest-BubbleBabble
%define name	perl-%{module}
%define version 0.01
%define release %mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Summary:	Create bubble-babble fingerprints
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Digest/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch

%description
Digest::BubbleBabble takes a message digest (generated by either of the MD5 or
SHA-1 message digest algorithms) and creates a fingerprint of that digest in
"bubble babble" format. Bubble babble is a method of representing a message
digest as a string of "real" words, to make the fingerprint easier to remember.
The "words" are not necessarily real words, but they look more like words than
a string of hex characters.

Bubble babble fingerprinting is used by the SSH2 suite (and, consequently, by
Net::SSH::Perl, the Perl SSH implementation) to display easy-to-remember key
fingerprints. The key (a DSA or RSA key) is converted into a textual form,
digested using Digest::SHA1, and run through bubblebabble to create the key
fingerprint.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Digest
%{_mandir}/man*/*

