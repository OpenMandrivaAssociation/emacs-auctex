%define	rname	auctex

Summary: 	Enhanced LaTeX mode for GNU Emacs
Name: 		emacs-auctex
Version: 	11.86
Release:	%mkrel 3
License: 	GPLv3+
Group: 		Editors
Source:		http://ftp.gnu.org/pub/gnu/auctex/auctex-%{version}.zip
URL: 		http://www.gnu.org/software/auctex/
Requires: 	emacs 
Requires: 	tetex-latex
BuildRequires: 	emacs-X11
BuildRequires: 	tetex-latex tetex-dvips
BuildArchitectures: noarch
BuildRoot: 	    %_tmppath/%name-build
Provides:	    %rname = %version-%release
Obsoletes:	    %rname
Provides: 	    preview-latex-common preview-latex-emacs
Obsoletes: 	    preview-latex-common preview-latex-emacs

%description
AUCTeX is a comprehensive customizable integrated environment for
writing input files for TeX, LaTeX, ConTeXt, Texinfo, and docTeX using
GNU Emacs.

%prep
%setup -q -n %rname-%version

%build
%configure --with-emacs
%make

%install
%__rm -rf %{buildroot}

install -d $RPM_BUILD_ROOT{%{_datadir}/emacs/site-lisp,%{_infodir}}
%makeinstall autodir=$RPM_BUILD_ROOT/var/lib/auctex

# This is already in tetex-latex:
%__rm -rf %buildroot%_datadir/texmf/tex/latex/preview
# What's this for?
%__rm -rf %buildroot/var/lib/auctex
# Don't install reference card:
%__rm -rf %buildroot%_datadir/doc/auctex

#perl -pi -e "s|$RPM_BUILD_ROOT||" $RPM_BUILD_ROOT/%_datadir/emacs/site-lisp/tex-site.el
install -d $RPM_BUILD_ROOT%_sysconfdir/emacs/site-start.d
echo "(if (string-match \"GNU Emacs\" (version)) (require 'tex-site))" >> $RPM_BUILD_ROOT%_sysconfdir/emacs/site-start.d/%rname.el

%post
%_install_info %rname

%preun
%_remove_install_info %rname

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc RELEASE COPYING INSTALL README TODO FAQ CHANGES
%_infodir/*
%_datadir/emacs/site-lisp/%rname
%_datadir/emacs/site-lisp/auctex.el
%_datadir/emacs/site-lisp/preview-latex.el
%_datadir/emacs/site-lisp/tex-site.el
%_datadir/texmf/doc/latex/styles/preview.dvi
%config(noreplace) %_sysconfdir/emacs/site-start.d/%{rname}*
