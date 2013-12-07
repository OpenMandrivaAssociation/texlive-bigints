# revision 29803
# category Package
# catalog-ctan /macros/latex/contrib/bigints
# catalog-date 2012-04-28 20:54:25 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-bigints
Version:	20120428
Release:	5
Summary:	Writing big integrals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bigints
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigints.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigints.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides facilities for drawing big integral signs
when needed. An example would be when the integrand is a
matrix.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bigints/bigints.sty
%doc %{_texmfdistdir}/doc/latex/bigints/Makefile
%doc %{_texmfdistdir}/doc/latex/bigints/README
%doc %{_texmfdistdir}/doc/latex/bigints/bigints.forlisting
%doc %{_texmfdistdir}/doc/latex/bigints/bigints.pdf
%doc %{_texmfdistdir}/doc/latex/bigints/bigints.tex
%doc %{_texmfdistdir}/doc/latex/bigints/perso.ist

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
