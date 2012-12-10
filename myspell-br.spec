Name: myspell-br
Summary: Breton hunspell dictionaries
Version: 0.3
Release: %mkrel 1
Group: System/Internationalization
URL: http://www.drouizig.org/
Source: http://extensions.services.openoffice.org/e-files/2207/3/dict-br_0.3.oxt
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

#Requires: hunspell
Requires: locales-br

%description
myspell-br contains spell checking data in Breton (France) to be used by
OpenOffice.org or MySpell-capable applications like Mozilla. With this
extension, you can compose a document in Breton and check for the typos easily.


%prep
%setup -q -c -n hunspell-br-%{version}

%build
chmod -x dictionaries/*

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/dict/{ooo,mozilla}
cp -p dictionaries/br_FR.* $RPM_BUILD_ROOT/%{_datadir}/dict/ooo
for ext in aff dic; do
	ln -s ../ooo/br.$ext $RPM_BUILD_ROOT/%{_datadir}/dict/mozilla/br.$ext
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSES-en.txt package-description.txt
%{_datadir}/dict/*



%changelog
* Sun Dec 12 2010 Thierry Vignaud <tv@mandriva.org> 0.3-1mdv2011.0
+ Revision: 620614
- import myspell-br

