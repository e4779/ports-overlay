# hlab overlay: llama.cpp master snapshot 2cbca38 (2026-11-03)
# WHY: quarterly pkg b10975 lacks arch support for nemotron-3.5-bolt (74b),
# deepseek-v4.1 and --models-memory-margin. This port bundles ggml from the
# same master tree (LLAMA_USE_SYSTEM_GGML off) WITH GGML_VULKAN=ON (the
# bundled ggml defaults Vulkan OFF — without this flag the binary has no
# GPU backend at all). FreeBSD Vulkan build needs the F_DUPFD shim (files/).
# Delete this overlay port when the official port bumps past the needed
# arch fixes; pkg upgrade will then prefer the official one (any future
# version > 10975.* wins).

PORTNAME=	llama-cpp
PORTVERSION=	10975.20261103.3
CATEGORIES=	misc # machine-learning
MASTER_SITES=	https://huggingface.co/buckets/ggml-org/llama-ui/resolve/${UI_ASSETS_TAG}/:ui_assets
DISTFILES=	dist.tar.gz:ui_assets \
		dist.tar.gz.sha256:ui_assets
DIST_SUBDIR=	llama-cpp-10975.20261103
EXTRACT_ONLY=	${DISTNAME}${EXTRACT_SUFX}

# hlab local override (upstream MAINTAINER yuri@FreeBSD.org)
MAINTAINER=	e4779@4779.ru
COMMENT=	LLM inference in C/C++ (hlab master snapshot) # '
WWW=		https://github.com/ggml-org/llama.cpp

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

# bundled ggml from the same master tree + its Vulkan build requirements
# (mirrors misc/ggml's VULKAN option deps)
BUILD_DEPENDS=	spirv-headers>0:graphics/spirv-headers \
		glslc:graphics/shaderc \
		vulkan-headers>0:graphics/vulkan-headers
LIB_DEPENDS=	libvulkan.so:graphics/vulkan-loader

USES=		cmake:testing compiler:c++11-lang python:run shebangfix ssl

BROKEN_armv7=	clang crashes, see https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=278810
BROKEN_i386=	compilation fails, see https://github.com/ggml-org/llama.cpp/issues/9545

USE_LDCONFIG=	yes

USE_GITHUB=	yes
GH_ACCOUNT=	ggml-org
GH_PROJECT=	llama.cpp
GH_TAGNAME=	2cbca389f515df455412dafa07e2b1359cc72a6d

SHEBANG_GLOB=	*.py

UI_ASSETS_TAG=	b10970

CMAKE_ON=	GGML_VULKAN=ON \
		BUILD_SHARED_LIBS \
		BUILD_STATIC_LIBS
CMAKE_OFF=	GGML_NATIVE \
		FREEBSD_ALLOW_ADVANCED_CPU_FEATURES \
		LLAMA_BUILD_TESTS \
		LLAMA_USE_SYSTEM_GGML
CMAKE_TESTING_ON=	LLAMA_BUILD_TESTS

# user for llama-server, only used when EXAMPLES=ON
USER=		nobody
SUB_LIST=	USER=${USER}

OPTIONS_DEFINE=		EXAMPLES
OPTIONS_DEFAULT=	EXAMPLES
OPTIONS_SUB=		yes

EXAMPLES_CMAKE_BOOL=	LLAMA_BUILD_EXAMPLES

BINARY_ALIAS=	git=false \
		python=${PYTHON_CMD} # for tests

post-patch:
	# set version in the code
	@${REINPLACE_CMD} \
		-e "s|set(BUILD_NUMBER 0)|set(BUILD_NUMBER 10975)|" \
		${WRKSRC}/cmake/build-info.cmake
	# update UI assets URL to point to fetched files
	@${REINPLACE_CMD} \
		-e "s|https://huggingface.co/buckets/.{HF_BUCKET}/resolve/.{resolved}|file://${DISTDIR}/${DIST_SUBDIR}|" \
		${WRKSRC}/scripts/ui-assets.cmake

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MEXAMPLES}
USE_RC_SUBR=	llama-server
.endif

.include <bsd.port.mk>
