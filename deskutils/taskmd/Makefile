PORTNAME=	taskmd
DISTVERSION=	0.8.1
PORTREVISION=	1
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
WRKSRC_SUBDIR=	apps/cli
GO_TARGET=	./cmd/taskmd
PLIST_FILES=	bin/taskmd
# Repo root carries a go.work (multi-module dev convenience); the port builds
# the single apps/cli module — workspace mode must not leak into the build.
GO_ENV+=	GOWORK=off

OPTIONS_DEFINE=	SKILLS
OPTIONS_DEFAULT=	SKILLS
SKILLS_DESC=	Install Agent Skills examples (SKILL.md per workflow)

.include <bsd.port.options.mk>

post-install:
.if ${PORT_OPTIONS:MSKILLS}
# Skills are vendored from claude-code-plugin@HEAD: the v0.8.1 tag predates
# the plugin directory, so the source archive does not carry them.
	${MKDIR} ${STAGEDIR}${EXAMPLESDIR}/skills
	${CP} -R ${FILESDIR}/skills/. ${STAGEDIR}${EXAMPLESDIR}/skills/
	${FIND} ${STAGEDIR}${EXAMPLESDIR}/skills -type d | ${SORT} -r | ${SED} "s,^${STAGEDIR},@dir ," >> ${TMPPLIST}
	${FIND} ${STAGEDIR}${EXAMPLESDIR}/skills -type f | ${SED} "s,^${STAGEDIR},," >> ${TMPPLIST}
.endif

# TODO(web): the web dashboard is not embedded in this package. Manual path:
#   cd apps/web && pnpm install && pnpm build
#   cp -R apps/web/dist apps/cli/internal/web/static/dist
#   go build -tags embed_web -o taskmd ./cmd/taskmd
# Port-level automation would need a nodejs prebuild stage (www/node22 builds
# from source in poudriere; bun has no FreeBSD build).

.include <bsd.port.mk>
