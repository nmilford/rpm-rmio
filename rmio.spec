Name:           rmio
Version:        0.0.1
Release:        1
Summary:        Sets up the repo.milford.io repository file and GPG Key.
License:        ASL
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildArch:      noarch
Group:          System Environment/Base
URL:            http://repo.milford.io
Obsoletes:      repo-milford-io

%description
Sets up the repo.milford.io repository file and GPG Key.

%install
install -d -m 755 %{buildroot}/%{_sysconfdir}/yum.repos.d/
install -d -m 755 %{buildroot}/%{_sysconfdir}/pki/rpm-gpg/

%{__cat} <<EOF > %{buildroot}/%{_sysconfdir}/yum.repos.d/rmio.repo
[rmio]
name=Packages from repo.milford.io
baseurl=http://repo.milford.io/el/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-RMIO
EOF

%{__cat} <<EOF > %{buildroot}/%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-RMIO
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1.4.5 (GNU/Linux)

mQGiBFHTc5IRBACezvyZu2qozcMeDK8A0lQO5J/qCAD2ujT7Wsu+DlNg4p8rOMAt
Ac6+IufemWZeg/Lb95Z6vZ+/pfMxsoQh9I9ZII7zrQR4SGb0g0iXWr9rkJ6UmEpl
YH8+dfnIhG8k29s+XnkaB7/694J4IP9gEyq+8KibYVVWJzBgc/8tG2y8YwCgse3D
gBoJTwa3VgHgnuYE6YDRedUD/3yVhQW8HdnDGsNMu3LQuSnox1AYG6804ak5v/X4
Kio7nn0Irc8pelFvJjbX91Zl+WGKehnlclFsTt0YYx8ti//zk+K/iY7zk3r3lNjG
Zhv3Nz4mVgfK/4NJnxlqJiDofHJpv6/mNRfd5LeLOfPEObAcx41PM7dAvZpPY+nt
F6GtBACBeZ+jDv/e6AGGp76yQRDxt29VA+ddOc9E4bC8pKA6lKjojDJ+VjPBdPqt
0xG+1BS8Zx8tXIA21grZb8D8dP/zw2PNhOZ/nT4H21GQbJ1HT9F8GdSJGhc2eZHw
HI0QTUE/Sc3hFAzjDLv2mOf2YB8LJvtIoa8OEVOIDP6vzH8unrQiTmF0aGFuIE1p
bGZvcmQgPG5hdGhhbkBtaWxmb3JkLmlvPohgBBMRAgAgBQJR03OSAhsDBgsJCAcD
AgQVAggDBBYCAwECHgECF4AACgkQDqQINpi7C9N/xQCeM32pvtnQ18ZnsFTCH14j
mpZrvugAn08T2qOGkXYuYjZcsWlrFXy7tzrLuQINBFHTc5sQCACgwBOzn2tA1qEU
d9zXm6dXJoSlYH134s7Eg4iA+UIlLM9gCgD+uP0jmZiycC1mV31Jj9Yzav/Hgsuk
E/tTingomdldLQhu/oDn41DwpOaiRtG1gLDquek9T2fOinyv+fqh3iqPs2bohZAS
vzuPLcU2K7hOVk5oOC5bvniKGxuBMLo21piv203LgSegUAqkaWsNIypxPNc6Ml1b
gSudIotQtevlWH/cz22Bb3WAnKL+AdUX27rEUwG9YRUyJaoKrE4LMsoeuVwklrZX
pbwBp2af9RiqTgHYn9o5lWvtvASgJvu5yg0sGD2Dy5C7VvfxkhBUzLKznCWrouWo
Eq5++LALAAMFB/99lGHK0vsnou+V+iRaasDjzU358knMihY9nXOStUsKOsAwwx+0
/ZQ9/ezYXCSmYhv3un7iI3s+hgYRWXVJ6WarFVaNri8HrkfLgJJg+gQL+ZzMCRiY
TYugnhs/XoY1zZ4NF8jpbdyQdjEQpb8lEowv5g95bbzE0uYNrunlwysFCmfncmVr
wgj2x80s2WKJUvgaelJPwBqZ0l3FbBfDSdJd2pE0MXv5oGmLo7tSUZRq7zgzId2/
ct79ZY2Q9swmgBwG+kE5UHnKYG8IGYTZD5ikFQzKyoXTIpaLTmOQZo0su7Y9An70
n/7ldcu9YTBwUQATJsfSZHK9FAy/FshplZsHiEkEGBECAAkFAlHTc5sCGwwACgkQ
DqQINpi7C9PGtgCfQn4FLJV9jr1cniVs3+aN36KbfIMAoKbN0Ra8FX28eiE+VyIH
0Lp74Fcf
=Trz2
-----END PGP PUBLIC KEY BLOCK-----
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sysconfdir}/yum.repos.d/rmio.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-RMIO

%changelog
* Tue Jul 02 2013 Nathan Milford <nathan@milford.io> 0.0.1
- First shot at a public/private repo.
