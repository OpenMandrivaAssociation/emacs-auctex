%define	rname	auctex

Summary: 	Enhanced LaTeX mode for GNU Emacs
Name: 		emacs-auctex
Version: 	11.87
Release:	4
License: 	GPLv3+
Group: 		Editors
Url: 		http://www.gnu.org/software/auctex/
Source0:	http://ftp.gnu.org/pub/gnu/auctex/auctex-%{version}.tar.gz
BuildRequires:	emacs
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRequires: texlive-latex-bin
Requires:	emacs
Requires:	tetex-latex
BuildArch:	noarch

%description
AUCTeX is a comprehensive customizable integrated environment for
writing input files for TeX, LaTeX, ConTeXt, Texinfo, and docTeX using
GNU Emacs.

%files
%doc RELEASE COPYING INSTALL README TODO FAQ CHANGES
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/%{rname}*
%{_datadir}/emacs/site-lisp/%{rname}
%{_datadir}/emacs/site-lisp/auctex.el
%{_datadir}/emacs/site-lisp/preview-latex.el
%{_datadir}/emacs/site-lisp/tex-site.el
%{_datadir}/texmf-dist/tex/latex/preview
%{_infodir}/*

#----------------------------------------------------------------------------

%prep
%setup -qn %{rname}-%{version}

%build
%configure --with-emacs
%make

%install
install -d %{buildroot}{%{_datadir}/emacs/site-lisp/site-start.d,%{_infodir}}
%makeinstall autodir=%{buildroot}/var/lib/auctex

# This is already in tetex-latex:
rm -rf %{buildroot}%{_datadir}/texmf/tex/latex/preview
# What's this for?
rm -rf %{buildroot}/var/lib/auctex
# Don't install reference card:
rm -rf %{buildroot}%{_datadir}/doc/auctex

#sed -i -e "s|%{buildroot}||" %{buildroot}/%{_datadir}/emacs/site-lisp/tex-site.el
install -d %{buildroot}%{_sysconfdir}/emacs/site-start.d
echo "(if (string-match \"GNU Emacs\" (version)) (require 'tex-site))" >> %{buildroot}%{_sysconfdir}/emacs/site-start.d/%{rname}.el


