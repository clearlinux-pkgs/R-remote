#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-remote
Version  : 1.2.1
Release  : 2
URL      : https://cran.r-project.org/src/contrib/remote_1.2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/remote_1.2.1.tar.gz
Summary  : Empirical Orthogonal Teleconnections in R
Group    : Development/Tools
License  : GPL-3.0
Requires: R-remote-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-gridExtra
Requires: R-latticeExtra
Requires: R-mapdata
Requires: R-raster
Requires: R-scales
BuildRequires : R-Rcpp
BuildRequires : R-gridExtra
BuildRequires : R-latticeExtra
BuildRequires : R-mapdata
BuildRequires : R-raster
BuildRequires : R-scales
BuildRequires : buildreq-R

%description
'remote' is short for 'R(-based) EMpirical Orthogonal TEleconnections'.
    It implements a collection of functions to facilitate empirical
    orthogonal teleconnection analysis. Empirical Orthogonal Teleconnections
    (EOTs) denote a regression based approach to decompose spatio-temporal
    fields into a set of independent orthogonal patterns. They are quite
    similar to Empirical Orthogonal Functions (EOFs) with EOTs producing
    less abstract results. In contrast to EOFs, which are orthogonal in both
    space and time, EOT analysis produces patterns that are orthogonal in
    either space or time.

%package lib
Summary: lib components for the R-remote package.
Group: Libraries

%description lib
lib components for the R-remote package.


%prep
%setup -q -c -n remote

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540773180

%install
export SOURCE_DATE_EPOCH=1540773180
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library remote
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library remote
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library remote
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library remote|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/remote/CITATION
/usr/lib64/R/library/remote/DESCRIPTION
/usr/lib64/R/library/remote/INDEX
/usr/lib64/R/library/remote/LICENSE
/usr/lib64/R/library/remote/Meta/Rd.rds
/usr/lib64/R/library/remote/Meta/data.rds
/usr/lib64/R/library/remote/Meta/features.rds
/usr/lib64/R/library/remote/Meta/hsearch.rds
/usr/lib64/R/library/remote/Meta/links.rds
/usr/lib64/R/library/remote/Meta/nsInfo.rds
/usr/lib64/R/library/remote/Meta/package.rds
/usr/lib64/R/library/remote/NAMESPACE
/usr/lib64/R/library/remote/R/remote
/usr/lib64/R/library/remote/R/remote.rdb
/usr/lib64/R/library/remote/R/remote.rdx
/usr/lib64/R/library/remote/data/australiaGPCP.RData
/usr/lib64/R/library/remote/data/datalist
/usr/lib64/R/library/remote/data/pacificSST.RData
/usr/lib64/R/library/remote/data/vdendool.RData
/usr/lib64/R/library/remote/help/AnIndex
/usr/lib64/R/library/remote/help/aliases.rds
/usr/lib64/R/library/remote/help/paths.rds
/usr/lib64/R/library/remote/help/remote.rdb
/usr/lib64/R/library/remote/help/remote.rdx
/usr/lib64/R/library/remote/html/00Index.html
/usr/lib64/R/library/remote/html/R.css
/usr/lib64/R/library/remote/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/remote/libs/remote.so
/usr/lib64/R/library/remote/libs/remote.so.avx2
/usr/lib64/R/library/remote/libs/remote.so.avx512
