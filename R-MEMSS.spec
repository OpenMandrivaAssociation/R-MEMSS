%global packname  MEMSS
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.9_0
Release:          2
Summary:          Data sets from Mixed-effects Models in S
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-0.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-lme4 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-lme4

%description
Data sets and sample analyses from Pinheiro and Bates, "Mixed-effects
Models in S and S-PLUS" (Springer, 2000).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
