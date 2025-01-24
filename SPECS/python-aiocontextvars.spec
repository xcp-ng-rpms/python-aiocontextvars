%global package_speccommit d6b7f7837e6978a917d805523268a780f8c5cd81
%global usver 0.2.2
%global xsver 3
%global xsrel %{xsver}%{?xscount}%{?xshash}
#
# spec file for package python-aiocontextvars
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define __python /usr/bin/python3
# IMPORTANT: This package is for python <= 3.6 only. If your package depends on
# python-aiocontextvars, make sure to only require it for these versions.
# Have a look into your upstream's setup.py or setup.cfg, they do the same.
Name:           python-aiocontextvars
Version:        0.2.2
Release:        %{?xsrel}%{?dist}
Summary:        Asyncio support for PEP-567 contextvars backport
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/fantix/aiocontextvars
Source0: aiocontextvars-0.2.2.tar.gz
#BuildRequires:  python3-contextvars
BuildRequires:  python3-setuptools
BuildRequires:  fdupes
BuildRequires:  python3-devel
BuildRequires:  python-rpm-macros
#BuildArch:      noarch

%description
In Python 3.5 and 3.6, this package added asyncio support to the PEP-567 backport
package also named contextvars, in a very different way than Python 3.7
contextvars implementation.

In Python 3.7 this package is 100% replaced by contextvars.

%prep
%autosetup -p1 -n aiocontextvars-%{version}

%build
echo "from setuptools import setup

setup(name=\"aiocontextvars\",
      version='%{version}',
     )" > ./setup.py
%py3_build

%install
%py3_install

# Copy source files to buildroot manually
mkdir -p %{buildroot}%{python_sitelib}/aiocontextvars
cp %{_builddir}/aiocontextvars-%{version}/aiocontextvars.py %{buildroot}%{python_sitelib}/
find %{buildroot}%{python_sitelib}/aiocontextvars

%if 0
%check
%pytest
%endif

%files -n %{name}
%license LICENSE
%doc README.rst AUTHORS.rst CONTRIBUTING.rst
%{python_sitelib}/aiocontextvars.py
%{python_sitelib}/__pycache__/aiocontextvars*.pyc
%{python_sitelib}/aiocontextvars-%{version}*-info


%changelog
* Mon Aug 19 2024 Marcus Granado <marcus.granado@cloud.com> - 0.2.2-3
- Bump release and rebuild

* Fri Aug 09 2024 Marcus Granado <marcus.granado@cloud.com> - 0.2.2-3
- Bump release and rebuild

* Fri Aug 09 2024 Marcus Granado <marcus.granado@cloud.com> - 0.2.2-3
- Bump release and rebuild

* Fri Aug 09 2024 Marcus Granado <marcus.granado@cloud.com> - 0.2.2-3
- Bump release and rebuild

* Fri Feb 23 2024 Rachel Yan <rachel.yan@citrix.com> - 0.2.2
- Initial import
