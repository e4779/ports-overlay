PORTNAME=	mg
PKGNAMESUFFIX=	-troglobit
PORTVERSION=	4.2
PORTREVISION=	1
CATEGORIES=	editors
MASTER_SITES=	https://github.com/troglobit/mg/releases/download/v${PORTVERSION}/
MAINTAINER=	e4779@4779.ru
COMMENT=	Small, fast Emacs-like editor: troglobit fork (UTF-8, modes, help)
WWW=		https://github.com/troglobit/mg
LICENSE=	PD
LICENSE_FILE=	${WRKSRC}/UNLICENSE

# оба порта ставят bin/mg; конфликт заявляем честно
CONFLICTS_INSTALL=	mg mg-static

USES=		ncurses
GNU_CONFIGURE=	yes
# бинарь ищет туториал по $docdir/tutorial.md, а PACKAGE_TARNAME=mg
CONFIGURE_ARGS=	--docdir=${PREFIX}/share/doc/mg \
		--with-startup=${PREFIX}/etc/mg

PLIST_FILES=	bin/mg \
		"@sample etc/mg.sample" \
		share/doc/mg/ChangeLog.md \
		share/doc/mg/README.md \
		share/doc/mg/UNLICENSE \
		share/doc/mg/tutorial.md \
		share/doc/mg/utf8.txt \
		share/man/man1/mg.1.gz

post-install:
	${INSTALL_DATA} ${WRKSRC}/doc/tutorial.md ${WRKSRC}/doc/utf8.txt \
		${STAGEDIR}${PREFIX}/share/doc/mg/
	${MKDIR} ${STAGEDIR}${PREFIX}/etc
	${INSTALL_DATA} ${WRKSRC}/doc/.mg ${STAGEDIR}${PREFIX}/etc/mg.sample

.include <bsd.port.mk>
