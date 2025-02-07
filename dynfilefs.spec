Name:           dynfilefs
Version: 1693308114.e94afcf
Release:        0
Summary:        Control over dynamically resizing file system
License:        GPL
Url:            https://github.com/Tomas-M/dynfilefs
Source0:        %{name}-%{version}.tar.gz

BuildRequires: fuse-devel
BuildRequires: gcc
BuildRequires: make
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: bash

%description
%{summary}.

%prep
%autosetup
bash ./autogen.sh
bash ./configure --sbindir='%_sbindir'

%build
make

%install
%make_install

%files
%{_sbindir}/dynfilefs
%doc README.md
%license LICENSE
