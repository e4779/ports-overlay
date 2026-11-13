PORTNAME=	taskmd
DISTVERSION=	0.8.1
PORTREVISION=	2
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
# Web dashboard assets: prebuilt with pnpm from the v0.8.1 sources and
# vendored in files/web-dist, embedded via the embed_web build tag
# (internal/web/embed.go //go:embed static/dist). Keeps poudriere pure-Go:
# no nodejs/pnpm dependency at package build time.
GO_BUILDFLAGS+=	-tags embed_web
PLIST_FILES=	bin/taskmd
# Repo root carries a go.work (multi-module dev convenience); the port builds
# the single apps/cli module — workspace mode must not leak into the build.
GO_ENV+=	GOWORK=off

OPTIONS_DEFINE=	SKILLS
OPTIONS_DEFAULT=	SKILLS
SKILLS_DESC=	Install Agent Skills examples (SKILL.md per workflow)

.include <bsd.port.options.mk>

# Populate the go:embed directory (gitignored upstream, absent from the
# source archive) before the build.
post-extract:
	${RM} -r ${WRKSRC}/internal/web/static
	${MKDIR} ${WRKSRC}/internal/web/static
	${CP} -R ${FILESDIR}/web-dist ${WRKSRC}/internal/web/static/dist

post-install:
.if ${PORT_OPTIONS:MSKILLS}
# Skills are vendored from claude-code-plugin@HEAD: the v0.8.1 tag predates
# the plugin directory, so the source archive does not carry them.
	${MKDIR} ${STAGEDIR}${EXAMPLESDIR}/skills
	${CP} -R ${FILESDIR}/skills/. ${STAGEDIR}${EXAMPLESDIR}/skills/
	${FIND} ${STAGEDIR}${EXAMPLESDIR}/skills -type d | ${SORT} -r | ${SED} "s,^${STAGEDIR},@dir ," >> ${TMPPLIST}
	${FIND} ${STAGEDIR}${EXAMPLESDIR}/skills -type f | ${SED} "s,^${STAGEDIR},," >> ${TMPPLIST}
.endif

# Web dashboard vendoring — regenerate files/web-dist for a new upstream
# version (pnpm 9: the lockfile is v9.0, pnpm 12 rejects it under
# --frozen-lockfile):
#   git clone --depth 1 -b v<v> https://github.com/driangle/taskmd /tmp/taskmd-src
#   cd /tmp/taskmd-src && corepack pnpm@9 install --frozen-lockfile
#   corepack pnpm@9 --dir apps/web build
#   rm -rf files/web-dist && cp -R apps/web/dist files/web-dist

.include <bsd.port.mk>
