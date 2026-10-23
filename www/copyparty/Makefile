PORTNAME=	copyparty
DISTVERSION=	1.20.26
CATEGORIES=	www
MASTER_SITES=	https://github.com/9001/copyparty/releases/download/v${DISTVERSION}/
DISTFILES=	copyparty-sfx.py
EXTRACT_ONLY=

MAINTAINER=	e4779@4779.ru
COMMENT=	Portable file server with a modern web UI (single-file sfx)

LICENSE=	MIT
WWW=		https://github.com/9001/copyparty

USES=		python:run
NO_BUILD=	yes
NO_ARCH=	yes

do-install:
	@${SED} -e '1s|^#!.*|#!${PYTHON_CMD}|' ${DISTDIR}/${DISTFILES} > ${STAGEDIR}${PREFIX}/bin/copyparty
	@${CHMOD} 0555 ${STAGEDIR}${PREFIX}/bin/copyparty

.include <bsd.port.mk>
