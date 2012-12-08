%define upstream_name	 Digest-BubbleBabble
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Create bubble-babble fingerprints
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Digest/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
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
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/man*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-4mdv2012.0
+ Revision: 765185
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-3
+ Revision: 763701
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-2
+ Revision: 667119
- mass rebuild

* Sat Mar 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.20.0-1
+ Revision: 648573
- update to new version 0.02

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.1
+ Revision: 403105
- rebuild using %%perl_convert_version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.01-8mdv2009.0
+ Revision: 223657
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.01-7mdv2008.1
+ Revision: 180385
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Dec 04 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-6mdv2007.0
+ Revision: 90378
- rebuild
- Import perl-Digest-BubbleBabble

* Wed Nov 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-5mdk
- spec cleanup
- better summary
- better description
- rpmbuildupdate aware
- fix directory owbership
- %%mkrel

* Sat Oct 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.01-4mdk
- rpmbuildupdated

