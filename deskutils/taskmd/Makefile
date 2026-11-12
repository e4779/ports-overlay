PORTNAME=	taskmd
DISTVERSION=	0.8.1
CATEGORIES=	deskutils
MAINTAINER=	e@4779.ru
COMMENT=	Markdown-native task tracking CLI for agents and humans
WWW=		https://github.com/driangle/taskmd

LICENSE=	MIT

USES=		go:1.26,modules
USE_GITHUB=	yes
GH_ACCOUNT=	driangle
GH_PROJECT=	taskmd
GH_TAGNAME=	v0.8.1
# Multi-module monorepo: the module lives in apps/cli, but upstream tags only
# the root (v0.8.1), so proxy.golang.org has no apps/cli@v0.8.1 entry — take
# go.mod from GitHub raw and let the build fetch deps from the network.
# @v0.8.1 is REQUIRED: without it the framework derives the version from
# DISTVERSION (0.8.1, no "v") and fetches .../taskmd/0.8.1/apps/cli/go.mod → 404,
# falls back to the codeload tar.gz as "go.mod" → gzip → parse error.
GO_MODULE=	github.com/driangle/taskmd/apps/cli@v0.8.1
GO_MOD_DIST=	github
GO_MOD_DIST=	github
WRKSRC_SUBDIR=	apps/cli
GO_TARGET=	./cmd/taskmd
# Repo root carries a go.work (multi-module dev convenience); the port builds
# the single apps/cli module — workspace mode must not leak into the build.
GO_ENV+=	GOWORK=off

PLIST_FILES=	bin/taskmd

# TODO: optional embedded web dashboard — upstream embeds the apps/web SPA
# (vite build) with -tags embed_web. Needs a nodejs/pnpm prebuild stage;
# this package ships the CLI only (taskmd web is unavailable).

.include <bsd.port.mk>
