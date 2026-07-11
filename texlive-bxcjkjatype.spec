%global tl_name bxcjkjatype
%global tl_revision 78793

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5a
Release:	%{tl_revision}.1
Summary:	Typeset Japanese with pdfLaTeX and CJK
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/japanese/BX/bxcjkjatype
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxcjkjatype.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxcjkjatype.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a working configuration of the CJK package,
suitable for Japanese typesetting of moderate quality. Moreover, it
facilitates use of the CJK package for pLaTeX users, by providing
commands that are similar to those used by the pLaTeX kernel and some
other packages used with it.

