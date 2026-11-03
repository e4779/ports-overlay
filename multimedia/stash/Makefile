PORTNAME=	stash
DISTVERSION=	0.32.0
PORTREVISION=	0
CATEGORIES=	multimedia
USE_GITHUB=	yes
GH_ACCOUNT=	e4779
GH_PROJECT=	stash
GH_TAGNAME=	v0.32.0-hlab.1

MAINTAINER=	e4779@4779.ru
COMMENT=	Web-based library organizer for adult media (hlab fork: hw-accelerated previews)
WWW=		https://github.com/e4779/stash

LICENSE=	AGPLv3

BUILD_DEPENDS=	go:lang/go
USES=		gmake

# ffmpeg нужен в рантайме (превью/спрайты/транскод), но RUN_DEPENDS не
# объявляем: poudriere-набор его не собирает (часы), приезжает из
# официального бинарного репо — рационал в runbook 10 (2026-10-23).

PLIST_FILES=	bin/stash
USE_RC_SUBR=	stash

# Ветка hlab-build несёт vendor/ и собранный ui/v2.5/build, поэтому сборка
# офлайн: go build -mod=vendor, без node/pnpm. STASH_VERSION/GITHASH/
# BUILD_DATE — оверрайды build-info (иначе gmake зовёт git, которого в
# GH-tarball нет).
do-build:
	cd ${WRKSRC} && ${SETENV} ${MAKE_ENV} GOTOOLCHAIN=local GOFLAGS=-mod=vendor \
		STASH_VERSION=v0.32.0-hlab.1 GITHASH=da9b4960 BUILD_DATE=2026-11-03T21:50:00+07:00 \
		gmake stash

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/stash ${STAGEDIR}${PREFIX}/bin/stash

.include <bsd.port.mk>
