PORTNAME=	stash
DISTVERSION=	0.31.1
PORTREVISION=	3
CATEGORIES=	multimedia
MASTER_SITES=	https://github.com/stashapp/stash/releases/download/v${DISTVERSION}/
DISTFILES=	stash-freebsd
EXTRACT_ONLY=

MAINTAINER=	e4779@4779.ru
COMMENT=	Web-based library organizer and viewer for adult media collections
WWW=		https://github.com/stashapp/stash

LICENSE=	AGPLv3

# ffmpeg нужен для превью/спрайтов/транскода, но НЕ объявляем RUN_DEPENDS:
# в poudriere-наборе фабрики его нет, а собирать его граф из исходников
# на N100 — часы. ffmpeg приезжает из официального бинарного репо
# (уже установлен на хосте); pkg резолвит его при установке stash.

NO_BUILD=	yes
USE_RC_SUBR=	stash

PLIST_FILES=	bin/stash \
		bin/stash-ffmpeg

do-install:
	${INSTALL_PROGRAM} ${DISTDIR}/${DISTFILES} ${STAGEDIR}${PREFIX}/bin/stash
	${INSTALL_SCRIPT} ${FILESDIR}/stash-ffmpeg ${STAGEDIR}${PREFIX}/bin/stash-ffmpeg

.include <bsd.port.mk>
