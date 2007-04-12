%define emacsver 21.4
%define	rname	auctex

Summary: 	Enhanced LaTeX mode for GNU Emacs
Name: 		emacs-auctex
Version: 	11.82
Release:	%mkrel 2
License: 	GPL
Group: 		Editors
Source0:        http://ftp.gnu.org/pub/gnu/auctex/auctex-%{version}.tar.bz2
URL: 		http://www.cs.auc.dk/~amanda/auctex/
Packager:       Pixel <pixel@mandrakesoft.com>
Requires: emacs = %emacsver
Requires: tetex-latex
BuildRequires: emacs-X11
BuildRequires: tetex-latex tetex-dvips
BuildArchitectures: noarch
BuildRoot: %_tmppath/%name-build
Provides:	%rname = %version-%release
Obsoletes:	%rname
Provides: preview-latex-common preview-latex-emacs
Obsoletes: preview-latex-common preview-latex-emacs

%description
AUC TeX is a comprehensive, customizable, integrated environment for
writing, editing and processing  input files for LaTeX using GNU Emacs. 

%prep
%setup -q -n %rname-%version

%build
%configure2_5x --with-emacs
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/emacs/site-lisp,%{_infodir}}
%makeinstall autodir=$RPM_BUILD_ROOT/var/lib/auctex

#gw already in tetex-latex
rm -rf %buildroot%_datadir/texmf/tex/latex/preview
#- what's this for?
rm -rf $RPM_BUILD_ROOT/var/lib/auctex

#perl -pi -e "s|$RPM_BUILD_ROOT||" $RPM_BUILD_ROOT/%_datadir/emacs/site-lisp/tex-site.el
install -d $RPM_BUILD_ROOT%_sysconfdir/emacs/site-start.d
echo "(if (string-match \"GNU Emacs\" (version)) (require 'tex-site))" >> $RPM_BUILD_ROOT%_sysconfdir/emacs/site-start.d/%rname.el

%post
%_install_info %rname

%preun
%_remove_install_info %rname

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc RELEASE COPYING INSTALL README TODO FAQ CHANGES
#%doc doc/tex-ref.pdf
%_infodir/*
%_datadir/emacs/site-lisp/%rname
%_datadir/emacs/site-lisp/auctex.el
%_datadir/emacs/site-lisp/preview-latex.el
%_datadir/emacs/site-lisp/tex-site.el
%_datadir/texmf/doc/latex/styles/preview.dvi
%config(noreplace) %_sysconfdir/emacs/site-start.d/%{rname}*


