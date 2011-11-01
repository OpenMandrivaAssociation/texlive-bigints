Name:		texlive-bigints
Version:	20100226
Release:	1
Summary:	Writing big integrals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bigints
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigints.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bigints.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides facilities for drawing big integral signs
when needed. An example would be when the integrand is a
matrix.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
