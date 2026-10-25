PORTNAME=	mg
DISTVERSION=	4.2
PORTREVISION=	1
PORTEPOCH=	2
CATEGORIES=	editors
MASTER_SITES=	https://github.com/troglobit/mg/releases/download/v${DISTVERSION}/
MAINTAINER=	e4779@4779.ru
COMMENT=	Small, fast Emacs-like editor (troglobit fork: UTF-8, modes, help)
WWW=		https://github.com/troglobit/mg
LICENSE=	PD
LICENSE_FILE=	${WRKSRC}/UNLICENSE
USES=		ncurses
GNU_CONFIGURE=	yes
PLIST_FILES=	bin/mg \
		share/doc/mg/ChangeLog.md \
		share/doc/mg/README.md \
		share/doc/mg/UNLICENSE \
		share/doc/mg/tutorial.md \
		share/man/man1/mg.1.gz

# C-h t ищет туториал по DOCDIR/tutorial.md; апстрим его не инсталлирует
post-install:
	${INSTALL_DATA} ${WRKSRC}/doc/tutorial.md ${STAGEDIR}${DOCSDIR}/tutorial.md

.include <bsd.port.mk>
