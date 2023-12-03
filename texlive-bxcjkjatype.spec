Name:		texlive-bxcjkjatype
Version:	67705
Release:	1
Summary:	Typeset Japanese with pdfLaTeX and CJK
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/bxcjkjatype
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxcjkjatype.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxcjkjatype.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a working configuration of the CJK
package, suitable for Japanese typesetting of moderate quality.
Moreover, it facilitates use of the CJK package for pLaTeX
users, by providing commands that are similar to those used by
the pLaTeX kernel and some other packages used with it.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bxcjkjatype
%doc %{_texmfdistdir}/doc/latex/bxcjkjatype

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
