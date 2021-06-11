Summary:	Python 2 binding for semanage library
Summary(pl.UTF-8):	Wiązania Pythona 2 do biblioteki semanage
Name:		python-semanage
Version:	2.9
Release:	4
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:	https://github.com/SELinuxProject/selinux/releases/download/20190315/libsemanage-%{version}.tar.gz
# Source0-md5:	25f086ff66175a0ca0e7b34dbe8586b7
URL:		https://github.com/SELinuxProject/selinux/wiki
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	flex
BuildRequires:	libselinux-devel >= 2.9
BuildRequires:	libsepol-devel >= 2.9
BuildRequires:	python-devel >= 2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	libsemanage >= %{version}
Requires:	python-selinux >= 2.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 binding for semanage library.

%description -l pl.UTF-8
Wiązania Pythona 2 do biblioteki semanage.

%prep
%setup -q -n libsemanage-%{version}

%build
%{__make} -j1 pywrap \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall -fno-strict-aliasing" \
	LIBDIR=%{_libdir} \
	LIBEXECDIR=%{_libexecdir} \
	PYPREFIX=python2 \
	PYTHON=%{__python}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-pywrap \
	LIBDIR=%{_libdir} \
	LIBEXECDIR=%{_libexecdir} \
	PYPREFIX=python2 \
	PYSITEDIR=%{py_sitedir} \
	PYTHON=%{__python} \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_semanage.so
%{py_sitedir}/semanage.py[co]
