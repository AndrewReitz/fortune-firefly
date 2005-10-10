Name:		fortune-firefly
Version:	1.8
Release:        2
Summary:	Quotes from the TV series "Firefly"

Group:		Amusements/Games
License:	GPL
URL:		http://www.daughtersoftiresias.org/progs/firefly/
#Source0:	http://www.daughtersoftiresias.org/progs/firefly/%{name}-%{version}.tar.bz2
Source1:	http://www.daughtersoftiresias.org/progs/firefly/fortune-firefly-%{version}/firefly
Source2:	http://www.daughtersoftiresias.org/progs/firefly/fortune-firefly-%{version}/README
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:	%{_sbindir}/strfile

Requires:	fortune-mod

%description
Fortune-firefly provides a set of quotes from the popular television series
"Firefly", and its movie "Serenity", by Joss Whedon.  

Quote authors include Tim Minear, Joss Whedon, Ben Edulund, Jane Esperson,
Drew Z. Greenberg, Jose Molina, Cheryl Cain, and Brent Matthews.

%prep
%setup -T -c
cp %{SOURCE1} ./firefly
cp %{SOURCE2} ./README

%build
# generate the firefly.dat file
%{_sbindir}/strfile firefly

%install
rm -rf $RPM_BUILD_ROOT
install -d m755 $RPM_BUILD_ROOT%{_datadir}/games/fortune
install -m644 firefly $RPM_BUILD_ROOT%{_datadir}/games/fortune/
install -m644 firefly.dat $RPM_BUILD_ROOT%{_datadir}/games/fortune/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/games/fortune/firefly
%{_datadir}/games/fortune/firefly.dat


%changelog

* Wed Oct 05 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.8.2
- Modified Source1 and Source2 to use URLs
- Minor quote corrections

* Tue Oct 04 2005 Michael A. Peters <mpeters@mac.com> - 1.8.1
- build .dat file in rpm
- install in %{_datadir}/games/fortune
- no need to use a tarball for two text files

* Tue Oct 04 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.8.1
- Took in some requested user-contributed quote corrections

* Mon Oct  3 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.7.2
- Added in README
- Repackaged without a nested tarball
- Incorporated specfile suggestions from Brian Pepple

* Mon Oct  3 2005 Karen Pease <meme@daughtersoftiresias.org> - 1.7.1
- Corrected/expanded some quotes

* Mon Oct  3 2005 Brian Pepple <bdpepple@ameritech.net> - 1.6-2
- Use some macros.
- Add fortune-mod requirement.
- Install into %%prefix, instead of %%datadir.
- Add prep, install, and clean sections.
- Add buildroot.

* Mon Oct 03 2005 Karen Pease <meme@daughtersoftiresias.org>
- Updated RPM package as per Fedora suggestions.

* Sat Oct 01 2005 Karen Pease <meme@daughtersoftiresias.org>
- Created RPM package; submitted to Fedora Extras.

* Fri Sep 30 2005 Karen Pease <meme@daughtersoftiresias.org>
- Added in preliminary quotes from Serenity; to be refined after transcripts are released.


