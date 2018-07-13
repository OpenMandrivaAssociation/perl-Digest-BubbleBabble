%define modname	Digest-BubbleBabble
%define modver	0.02

Summary:	Create bubble-babble fingerprints
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	16
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Digest/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl(inc::Module::Install)
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Digest
%{_mandir}/man3/*

