PORTNAME=	photofield
DISTVERSION=	0.9.4.g20261108
CATEGORIES=	www
USE_GITHUB=	yes
GH_ACCOUNT=	SmilyOrg
GH_PROJECT=	photofield
GH_TAGNAME=	d7374a9

MAINTAINER=	e4779@4779.ru
COMMENT=	Fast self-hosted photo gallery with EXIF timeline (no ML, single binary)
WWW=		https://github.com/SmilyOrg/photofield

LICENSE=	MIT

# node: для vite-сборки UI (node_modules приезжает дистфайлом :ui —
# npm-registry из джейла недоступна: c-ares под nobody не резолвит).
# vite вшивает собранный dist в бинарь только с тегом embedui (иначе
# StaticFs пустой и / отвечает 404 — молча, без ошибок сборки).
BUILD_DEPENDS=	node:www/node
USES=		go:1.26,modules

# go.mod из raw.git того же коммита; модули качаются в fetch-фазе в
# distfiles-кеш, vendor собирается go-post-extract -> сборка оффлайн.
GO_MODULE=	github.com/SmilyOrg/photofield@d7374a9
GO_MOD_DIST=	github
GO_BUILDFLAGS+=	-tags embedui
CGO_ENABLED=	0

DISTFILES+=	photofield-ui-deps-${DISTVERSION}.tar.gz:ui
MASTER_SITES+=	file:///srv/homelab/ports-overlay/www/photofield/:ui

# ffmpeg/ffprobe нужны в рантайме (превью видео), но RUN_DEPENDS не
# объявляем: приезжает из официального бинарного репо (runbook 10).

PLIST_FILES=	bin/photofield
USE_RC_SUBR=	photofield

pre-build:
	cd ${WRKSRC}/ui && ${TAR} xf ${DISTDIR}/${DIST_SUBDIR}/photofield-ui-deps-${DISTVERSION}.tar.gz
	cd ${WRKSRC}/ui && ${SETENV} ${MAKE_ENV} node_modules/.bin/vite build

.include <bsd.port.mk>
